# Mock Patient Data Generation

This Python script generates mock patient data including patient information, credit card data, and patient addresses for use in data analysis and visualization projects. It utilizes the Faker library to create realistic-looking data.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- Faker library (`pip install Faker`)
- NumPy library (`pip install numpy`)
- Pandas library (`pip install pandas`)
- pyzipcode library (`pip install pyzipcode`)

## Usage

1. Clone or download this repository to your local machine.

2. Navigate to the directory containing the Python script (`mock_patient_data.py`).

3. Run the script using Python:

python PatientMaker.ipynb

4. Enter the number of patients you want to generate when prompted.

5. The script will generate patient data, credit card data, and patient addresses, and save them as CSV files in the specified folder path.

## Output

The script generates the following CSV files:

- `patient_data.csv`: Contains patient information including first name, last name, date of birth, age, gender, and medical record number.

- `credit_card_data.csv`: Contains credit card information associated with each patient, including credit card number, expiration date, and CVV.

- `patient_address.csv`: Contains patient addresses including street address, city, state, and ZIP code.

## Folder Structure

The generated CSV files will be saved in the specified folder path. If the folder doesn't exist, the script will create it.

## Additional Files
- `Dashboard.pdf`: PDF file containing the dashboard created from the generated data using PowerBi.
- `activate.bat`: Windows batch file used with task scheduler on Windows to auto-run the `GenerateEncounter` Jupyter notebook.

## Note

This script was created to gain experience in uploading data to MySQL and pulling that data into PowerBI for creating semantic models and analysis.

This script is intended for generating mock data for testing and demonstration purposes only. It does not contain real patient information. If any names or dates of birth match any real person it is purely coincidental.
