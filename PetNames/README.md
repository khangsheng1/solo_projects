# Generating Pet Names and Uploading to SQL

This repository contains a Python script that generates fake pet names and saves them into a CSV file. It also includes another script to upload the generated pet names from the CSV file into an SQL table.

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.x
- pandas
- faker
- mysql-connector-python

You can install the required Python libraries using pip:

```bash
pip install pandas faker mysql-connector-python

## Extra

This doesn't make a folder or anything for the generated CSV files, nor does it set up a database for you in SQL. That will have to be done manually. The script will ask where you want to save files and you may have to edit the code to fit your SQL database.
