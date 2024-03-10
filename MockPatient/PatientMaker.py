from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker and seed random number generator
fake = Faker()
random.seed(42)

# Function to generate random date within a range
def random_date(start_date, end_date):
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

# Generate patient data
def generate_patient_data(num_patients):
    patients = []
    current_date = datetime.now()
    start_date = current_date - timedelta(days=365*80)  # 80 years ago
    end_date = current_date - timedelta(days=1)        # Yesterday

    for _ in range(num_patients):
        name = fake.name()
        dob = fake.date_of_birth(minimum_age=1, maximum_age=100)
        medical_record_number = fake.unique.random_number(digits=8)
        gender = random.choice(['Male', 'Female'])
        last_encounter_date = random_date(start_date, end_date)
        age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))

        patients.append({
            'Name': name,
            'Date of Birth': dob.strftime('%Y-%m-%d'),
            'Medical Record Number': medical_record_number,
            'Age': age,
            'Gender': gender,
            'Last Hospital Encounter': last_encounter_date.strftime('%Y-%m-%d')
        })
    return patients

# Example usage to generate 10 patient records
if __name__ == "__main__":
    num_patients = 10
    patient_data = generate_patient_data(num_patients)
    for patient in patient_data:
        print(patient)
