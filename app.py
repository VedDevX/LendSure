from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the saved model
best_model = joblib.load('random_forest_model.pkl')

# Function to convert string inputs to binary
def convert_input_to_binary(user_input, options):
    return options.get(user_input, -1)  # Return -1 for invalid inputs

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Collect user inputs
        gender_input = request.form['gender']
        married_input = request.form['married']
        dependents_input = request.form['dependents']
        education_input = request.form['education']
        self_employed_input = request.form['self_employed']
        credit_history_input = request.form['credit_history']
        property_area_input = request.form['property_area']
        applicant_income = float(request.form['applicant_income'])
        loan_amount = float(request.form['loan_amount'])
        loan_amount_term = float(request.form['loan_amount_term'])

        # Convert string inputs to binary format
        gender = convert_input_to_binary(gender_input, {'Male': 0, 'Female': 1})
        married = convert_input_to_binary(married_input, {'Yes': 1, 'No': 0})
        dependents_numeric = int(dependents_input) if dependents_input != '3+' else 3
        education = convert_input_to_binary(education_input, {'Graduate': 1, 'Not Graduate': 0})
        self_employed = convert_input_to_binary(self_employed_input, {'Yes': 1, 'No': 0})
        credit_history = convert_input_to_binary(credit_history_input, {'Yes': 1, 'No': 0})
        property_area = convert_input_to_binary(property_area_input, {'Rural': 0, 'Semiurban': 1, 'Urban': 2})

        # Calculate Total Applicant Income
        Total_Applicant_Income = applicant_income + loan_amount

        # Apply log transformations
        ApplicantIncomeLog = np.log(applicant_income + 1)  # Avoid log(0)
        LoanAmountLog = np.log(loan_amount + 1)  # Avoid log(0)
        Loan_Amount_Term_Log = np.log(loan_amount_term + 1)  # Avoid log(0)
        Total_Applicant_Income_Log = np.log(Total_Applicant_Income + 1)  # Avoid log(0)

        # Create DataFrame from user input with matching feature names
        input_data = pd.DataFrame({
            'Gender': [gender],
            'Married': [married],
            'Dependents': [dependents_numeric],
            'Education': [education],
            'Self_Employed': [self_employed],
            'Credit_History': [credit_history],
            'Property_Area': [property_area],
            'Total_Applicant_Income': [Total_Applicant_Income],
            'ApplicantIncomelog': [ApplicantIncomeLog],       
            'LoanAmountLog': [LoanAmountLog],                
            'Loan_Amount_Term_Log': [Loan_Amount_Term_Log],      
            'Total_Applicant_Income_Log': [Total_Applicant_Income_Log]
        })

        # Make prediction
        prediction = best_model.predict(input_data)
        status = prediction[0]

        if status == 0:
            result = "Rejected"
            adjusted_loan_amount = 0.0  # No loan amount if rejected
        elif status == 1:
            result = "Approved"
            # Calculate adjusted loan amount based on the number of dependents
            adjustment_factor = max(0.7, 1 - (0.1 * dependents_numeric))  # Minimum adjustment factor is 0.7 (30% reduction)
            adjusted_loan_amount = loan_amount * adjustment_factor

        # Add data to test.csv file
        data_to_save = {
            'Gender': gender_input,
            'Married': married_input,
            'Dependents': dependents_input,
            'Education': education_input,
            'Self_Employed': self_employed_input,
            'Credit_History': credit_history_input,
            'Property_Area': property_area_input,
            'Applicant_Income': applicant_income,
            'Loan_Amount': loan_amount,
            'Loan_Amount_Term': loan_amount_term,
            'Loan_Status': result,
            'Eligible_Loan_Amount': adjusted_loan_amount
        }

        # Create or append the CSV file
        df = pd.DataFrame([data_to_save])
        if not os.path.isfile('test.csv'):
            df.to_csv('test.csv', index=False)
        else:
            df.to_csv('test.csv', mode='a', header=False, index=False)

        return render_template('result.html', result=result, eligible_loan_amount=adjusted_loan_amount)

# Route to view test.csv file
@app.route('/view_data', methods=['GET'])
def view_data():
    try:
        # Load the CSV file
        data = pd.read_csv('test.csv')
        is_empty = data.empty  # Check if the DataFrame is empty
        return render_template('view_data.html', data=data, is_empty=is_empty)
    except FileNotFoundError:
        return "The file 'test.csv' does not exist yet."

if __name__ == '__main__':
    app.run(debug=True)
