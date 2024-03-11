# Project Notebook: solo_projects

Welcome to the GitHub repository for our project notebook! This repository contains a set of Jupyter Notebooks aimed at generating fake data sets, uploading them to a SQL database, and subsequently analyzing the data in Power BI. This README will guide you through the contents of the repository and how to use the notebooks effectively.

## Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Notebook Descriptions](#notebook-descriptions)
5. [License](#license)

## Introduction
This project aims to demonstrate a workflow for generating synthetic data, uploading it to a SQL database, and performing analysis using Power BI. Synthetic data generation is particularly useful in scenarios where real data may not be available or cannot be shared due to privacy concerns.

## Setup
To use the notebooks in this repository, you'll need to have the following prerequisites installed:
- Python (>=3.6)
- Jupyter Notebook
- SQLAlchemy
- Pandas
- Faker

You'll also need access to a SQL database (e.g., MySQL, PostgreSQL) and Power BI Desktop.

## Usage
1. Clone this repository to your local machine:

git clone https://github.com/khangsheng1/solo_projects


2. Install the required Python dependencies:

pip install -r requirements.txt


3. Open the Jupyter Notebook server:

jupyter notebook


4. Navigate to the notebook you wish to run and execute the cells as instructed.

5. Once you have generated the fake data and uploaded it to your SQL database, you can connect to the database using Power BI and perform analysis.

## Notebook Descriptions
- **01_Data_Generation.ipynb**: This notebook demonstrates how to generate synthetic data using the Faker library.
- **02_SQL_Upload.ipynb**: This notebook guides you through the process of uploading the generated data to a SQL database using SQLAlchemy.
- **03_PowerBI_Analysis.pbix**: This Power BI file contains pre-configured connections to the SQL database and visualizations for data analysis.

## License
This project is licensed under the [MIT License](LICENSE).

Feel free to contribute to this project by submitting pull requests or opening issues for any suggestions or problems you encounter.

Happy coding! 🚀
