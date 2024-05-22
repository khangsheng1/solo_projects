import mysql.connector
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from datetime import datetime

passcode = input("What is your password?: ")

def determine_reason_for_encounter(age, gender):
    if age <= 18:
        reasons = [
            "Infectious diseases",
            "Accidents and injuries",
            "Childhood illnesses",
            "Appendicitis"
        ]
    elif age <= 64:
        reasons = [
            "Pregnancy and childbirth" if age < 35 and gender == "Female" and random.random() < (35 - age) / 35 else None,
            "Accidents and injuries",
            "Chronic illnesses",
            "Mental health concerns",
            "Surgery"
        ]
    else:
        reasons = [
            "Chronic illnesses",
            "Falls and fractures",
            "Pneumonia",
            "Complications from surgery"
        ]

    # Filter out None values and select a random reason
    reasons = [reason for reason in reasons if reason is not None]
    selected_reason = random.choice(reasons) if reasons else "Reason not specified"

    return selected_reason
def table_exists(cursor, table_name):
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return cursor.fetchone() is not None
def upload_to_mysql(dataframe, table_name, passcode):
    # Establish connection to MySQL Database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=passcode,
        database="mock_patient_project"
    )
    cursor = connection.cursor()

    try:
        # Check if table exists
        if not table_exists(cursor, table_name):
            print(f"Table '{table_name}' does not exist.")
            return
        print(f"Table '{table_name}' exists.")

        # Iterate over each row in the DataFrame and insert it into the MySQL table
        for index, row in dataframe.iterrows():
            # Prepare column names string
            columns_str = ', '.join(dataframe.columns)

            # Prepare placeholders for data values
            placeholders = ', '.join(['%s'] * len(row))

            # Convert timestamp to string with desired format
            row_values = [str(value) if not isinstance(value, pd.Timestamp) else value.strftime('%Y-%m-%d') for value in row]

            # Construct SQL query for row insertion
            sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"

            # Execute SQL query with row data
            cursor.execute(sql, tuple(row_values))

        # Commit changes
        connection.commit()

    except Exception as e:
        print("Error during insertion:", e)
        connection.rollback()

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()
population = 200000
years = 40
encounter_rate_per_year = 2
mortality_rate = 0.008  # 0.8% per year

total_encounters = 0
for year in range(years):
    population_alive = population * (1 - mortality_rate) ** year
    encounters_this_year = population_alive * encounter_rate_per_year
    total_encounters += encounters_this_year

total_encounters = total_encounters/10
print("Total encounters over 40 years:", int(total_encounters))
# Database connection details
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=passcode,
    database="mock_patient_project"
)
cursor = connection.cursor()

# Fetch all data from patient_data table
cursor.execute("SELECT * FROM patient_data")

# Fetch the column names
column_names = [desc[0] for desc in cursor.description]

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Create a DataFrame from the fetched data
patients = pd.DataFrame(rows, columns=column_names)

# Close the cursor and connection
cursor.close()
connection.close()

# Display the first few rows of the DataFrame
# print(patients.head())
# Define age group percentages that goes to hospitals
age_groups = [
    (0, 18, 0.125),  # 12.5% for age 0 to 18
    (19, 34, 0.175), # 17.5% for age 19 to 34
    (35, 65, 0.3),   # 30% for age 35 to 65
    (66, 120, 0.4)   # 40% for age 66+
]

# Initialize dictionaries to store patients for each age group
patients_by_age_groups = {}

# Iterate over age groups and filter patients accordingly
for min_age, max_age, _ in age_groups:
    age_group_name = f"Age_{min_age}_to_{max_age}"
    filtered_patients = patients[(patients['Age'] >= min_age) & (patients['Age'] <= max_age)]
    patients_by_age_groups[age_group_name] = filtered_patients

# # Separate patients into individual DataFrames for each age group
# patients_0_to_18 = patients_by_age_groups['Age_0_to_18']
# patients_19_to_34 = patients_by_age_groups['Age_19_to_34']
# patients_35_to_65 = patients_by_age_groups['Age_35_to_65']
# patients_66_plus = patients_by_age_groups['Age_66_to_120']

# Define function to select a group based on age group probabilities
def select_age_group(age_groups):
    group_names = [f"Age_{min_age}_to_{max_age}" for min_age, max_age, _ in age_groups]
    probabilities = [prob for _, _, prob in age_groups]
    selected_group = random.choices(group_names, weights=probabilities, k=1)[0]
    return selected_group

# Example usage:
# selected_age_group = select_age_group(age_groups)
# print("Selected Age Group:", selected_age_group)
# selected_group = select_age_group(age_groups)
    
# # Draw a random patient from the selected age group
# if not patients_by_age_groups[selected_group].empty:
#     random_patient = patients_by_age_groups[selected_group].sample(n=1)
#     print(random_patient)
# else:
#     raise ValueError(f"No patients available in the selected age group: {selected_group}")

# Function to fetch patient info
def fetch_patient_info(age_groups, patients_by_age_groups, num_records_to_fetch):
    selected_patients = []

    for i in range(num_records_to_fetch):
        selected_group = select_age_group(age_groups)
        
        # Draw a random patient from the selected age group
        if not patients_by_age_groups[selected_group].empty:
            random_patient = patients_by_age_groups[selected_group].sample(n=1)
            selected_patients.append(random_patient)
        else:
            raise ValueError(f"No patients available in the selected age group: {selected_group}")
        
        # Print iteration number every 100000 iterations
        if (i + 1) % 100 == 0:
            print(f"Iteration number: {i + 1} complete")

    # Concatenate all DataFrames at once
    selected_patients_df = pd.concat(selected_patients, ignore_index=True)
    return selected_patients_df

# # Example usage
# num_records_to_fetch = 100000
# selected_patients = fetch_patient_info(age_groups, patients_by_age_groups, num_records_to_fetch)
# print(selected_patients)
def generate_past_encounters(selected_patients):
    today = datetime.now().date()
    # Create a new DataFrame to store the results
    encounter_data = []
    num_records = len(selected_patients)
    for i in range(num_records):
        current_Patient = selected_patients.iloc[i]
        date_of_birth = current_Patient['DateOfBirth']
        
        # Generate a random encounter date between two days ago and the date of birth
        max_days_back = (today - date_of_birth.date()).days - 2
        encounter_date = today - timedelta(days=random.randint(2, max_days_back))
        # Calculate the patient's age at the encounter date
        encounter_age = (encounter_date - date_of_birth.date()).days // 365
        
        # Determine the reason for encounter
        reason_for_encounter = determine_reason_for_encounter(encounter_age, current_Patient['Gender'])
        
        # Append the encounter data to the list
        encounter_data.append({
            'FirstName': current_Patient['FirstName'],
            'LastName': current_Patient['LastName'],
            'Name': current_Patient['Name'],
            'DateOfBirth': current_Patient['DateOfBirth'],
            'Age': current_Patient['Age'],
            'Gender': current_Patient['Gender'],
            'MedicalRecordNumber': current_Patient['MedicalRecordNumber'],
            'EncounterDate': encounter_date,
            'ReasonForEncounter': reason_for_encounter
        })
            
    # Create a DataFrame from the encounter data
    encounters = pd.DataFrame(encounter_data)
    return encounters

print(type(int(total_encounters)))
selected_patients = fetch_patient_info(age_groups, patients_by_age_groups, int(total_encounters))
encounters = generate_past_encounters(selected_patients)
encounters['EncounterDate'] = pd.to_datetime(encounters['EncounterDate']).dt.date
encounters['ReasonForEncounter'] = encounters['ReasonForEncounter'].astype(str)
upload_to_mysql(encounters, 'encounters', passcode)