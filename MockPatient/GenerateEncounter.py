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
def generate_percentage():
    # Generate a random number from a normal distribution centered around 0.15
    # with a standard deviation that controls the spread of the bell curve
    mean = 0.015
    std_dev = 0.005  # Adjust this value to control the spread of the bell curve
    percentage = np.random.normal(mean, std_dev)
    
    # Ensure the generated percentage falls within the desired range [0.1, 0.2]
    percentage = max(0.01, min(0.02, percentage))
    
    return percentage

# Call the function to generate the percentage
# percentage_to_fetch = generate_percentage()

# print("Generated Percentage:", percentage_to_fetch)

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
# Set the percentage of records to fetch
percentage_to_fetch = generate_percentage()  # Change this percentage as needed

# Establish connection to MySQL Database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=passcode,
    database="mock_patient_project"
)
cursor = connection.cursor()

try:
    # Get total number of records in patient_data table
    cursor.execute("SELECT COUNT(*) FROM patient_data")
    total_records = cursor.fetchone()[0]

    # Calculate the number of records to fetch based on the percentage
    num_records_to_fetch = int(total_records * (percentage_to_fetch / 100))

    # Call the function to fetch patient info with the specified number of entries
    patient_info_df = selected_patients = fetch_patient_info(age_groups, patients_by_age_groups, int(num_records_to_fetch))

    # Determine reason for encounter based on age and gender for each fetched record
    for index, row in patient_info_df.iterrows():
        age = row['Age']
        gender = row['Gender']
        reason_for_encounter = determine_reason_for_encounter(age, gender)
        # Add reason for encounter and today's date to the DataFrame
        patient_info_df.at[index, 'ReasonForEncounter'] = reason_for_encounter
        patient_info_df.at[index, 'EncounterDate'] = datetime.now().strftime("%Y-%m-%d")

    # Print the DataFrame
    print(patient_info_df)

finally:
    # Close cursor and connection
    cursor.close()
    connection.close()
upload_to_mysql(patient_info_df, 'encounters', passcode)