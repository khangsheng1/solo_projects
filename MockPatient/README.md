# Fake Patient Information Generator

This repository contains Python scripts for generating fake patient information and storing it in a MySQL database.

## Overview

The scripts utilize the Faker library to generate realistic fake patient data including names, dates of birth, genders, and medical record numbers. It also includes functionality to generate random patient encounters with chief complaints and encounter dates.

## Prerequisites

- Python 3.x
- MySQL database server
- MySQL Connector/Python library
- Faker library
- Pytz library (if using timezone handling)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install MySQL database server from [mysql.com](https://www.mysql.com/downloads/).
3. Install the necessary Python libraries using pip:

    ```
    pip install mysql-connector-python faker pytz
    ```

4. Clone this repository:

    ```
    https://github.com/khangsheng1/solo_projects/tree/main/MockPatient
    ```

## Usage

1. Modify the connection parameters in the Python scripts (`generate_patient_data.py`, `generate_encounters.py`) to match your MySQL database configuration.
2. Run the Python scripts to generate fake patient information and encounters:

    ```
    python generate_patient_data.py
    python generate_encounters.py
    ```

3. Verify that the data has been inserted into your MySQL database.

## Files

- `generate_patient_data.py`: Python script to generate fake patient data.
- `generate_encounters.py`: Python script to generate fake patient encounters.
- `README.md`: This README file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

