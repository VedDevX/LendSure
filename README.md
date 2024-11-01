# LendSure: Bank Loan Approval Prediction

LendSure is a machine learning application built with Flask that predicts bank loan approval based on various applicant details. It features a user-friendly, responsive interface for data input and visualization, enhancing the decision-making process for loan eligibility. This project combines advanced CSS styling and a detailed UI layout to improve readability, usability, and aesthetic appeal.

## Project Description

LendSure aims to predict whether a loan applicant is eligible for a loan based on various factors, including income, marital status, credit history, and property location. The project employs a supervised machine learning model trained on a dataset of 614 entries and 13 attributes. This dataset includes critical features like `ApplicantIncome`, `CoapplicantIncome`, and `Credit_History`, enabling the prediction model to make informed decisions on loan approvals.

## Project Files

### 1. `app.py`

This is the main application file for the Flask framework, handling:
   - **Routing**: Manages multiple routes for data input, data view, and prediction results.
   - **Form Handling**: Captures and validates user inputs, then sends data to the prediction model.
   - **Data Display**: Passes prediction results and loan eligibility details to the frontend.
   - **Model Integration**: Imports the trained machine learning model from the Jupyter Notebook to predict loan eligibility based on user inputs.

### 2. `predict_loan.ipynb`

This Jupyter Notebook contains the data processing and machine learning pipeline used to train the model. Key steps in the pipeline include:
   - **Data Preprocessing**: Cleaning data by detecting outliers and filling null values, ensuring data quality for training.
   - **Feature Engineering**: Visualizes key relationships (e.g., number of loans by applicant gender and marital status).
   - **Model Training and Evaluation**: Uses classification algorithms to train the model and tests its accuracy, optimizing for reliable predictions.
   - **Model Export**: Saves the trained model as a file for integration with the Flask app.

### 3. `view_data.html`

An HTML template to render the applicant loan data in a structured and responsive table format. This file is designed for optimal readability, including:
   - **Table Styling**: Uses a clean, green-accented color scheme with alternate row shading and hover effects for clarity.
   - **Responsive Layout**: Enables horizontal scrolling on smaller screens to ensure all data fields are viewable.
   - **Dynamic Message Display**: Shows a 'No data available' message when there’s no data to display, maintaining the clean design.

### 4. `style.css`

The primary CSS file that brings visual appeal and responsive styling to the application. It includes:
   - **Form and Button Styling**: A green-accented, rounded style for buttons and inputs, giving a modern look.
   - **Responsive Adjustments**: Adapts font sizes, input field spacing, and layout for various screen sizes.
   - **Color Scheme and Consistency**: A consistent gradient background with green and white accents enhances readability and visual hierarchy.

## Dataset Description

The dataset comprises 13 columns, with key features like:
   - **Gender**: Applicant’s gender (Male/Female)
   - **Married**: Marital status of the applicant
   - **Dependents**: Number of dependents
   - **Education**: Education level (Graduate/Not Graduate)
   - **Self_Employed**: Self-employment status
   - **ApplicantIncome**: Monthly income of the applicant
   - **CoapplicantIncome**: Monthly income of the co-applicant
   - **LoanAmount**: Loan amount requested
   - **Loan_Amount_Term**: Duration of loan repayment (in months)
   - **Credit_History**: Credit history (1 for good credit history, 0 for bad)
   - **Property_Area**: Area of the property (Urban, Semiurban, Rural)
   - **Loan_Status**: Indicates loan approval status (Y/N)

## Features

1. **Loan Prediction Form**: A user-friendly form collects inputs, such as applicant income, loan amount, and credit history, to predict loan eligibility.
2. **Data Display Table**: A structured and responsive table showcases the processed data, making it easy to review and understand applicant details.
3. **Responsive UI**: Styled with CSS, ensuring accessibility and aesthetic quality across devices of all screen sizes.

## Project Setup and Execution

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd lendSure

2. **Install Requirements: Install necessary Python packages using requirements.txt**:
   ```bash
   pip install -r requirements.txt

3. **Run Flask Application: Start the Flask server to run the app:**
   ```bash
   python app.py
The app will be accessible at http://127.0.0.1:5000 (May differ when you run this code).

4. **Access the Application:**
   1. **Home Page:** Enter applicant details for loan prediction.
   2. **Data View:** View all applicant data in a responsive table format.
  
## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for more details.
