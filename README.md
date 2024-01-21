# Finzome_Assignments
Solutions to the Task 1&amp;2 in the assigned Finzome Challenge

# Financial Data Volatility Calculation (Task 1)

This repository contains Python code for calculating daily and annualized volatility from a financial dataset. The dataset is expected to be in **CSV** format, and the calculations are performed using Python with the help of Pandas and NumPy libraries.

## Table of Contents
- [Introduction](#introduction)
- [Calculations](#calculations)
- [Tech Stack](#tech-stack)
- [Usage](#usage)
- [Sample Dataset](#sample-dataset)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The purpose of this project is to provide a Python script for calculating daily and annualized volatility from a given financial data. It uses standard financial formulas and makes use of Pandas and NumPy for efficient calculations.

## Calculations

The key calculations performed by the script include:

1. **Daily Returns:**
   - Formula: `(current close / previous close) - 1`

2. **Daily Volatility:**
   - Formula: `Standard Deviation (Daily Returns)`

3. **Annualized Volatility:**
   - Formula: `Daily Volatility * Square Root (length of data)`

## Tech Stack

- [Python](https://www.python.org/): The programming language used for the script.
- [Pandas](https://pandas.pydata.org/): A powerful data manipulation library for Python.
- [NumPy](https://numpy.org/): A library for mathematical operations in Python.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Ojas21/Finzome_Assignments.git
   cd Finzome_Assignment
2. Adding the path:
   - change the path in 'file-path' to your local system one
3.Run the Python script:
   ```bash
     python Ojas21/Finzome_Assignments.py

## Sample Dataset
The sample dataset used for testing the script is available in the **data** directory. You can replace it with your own financial dataset. by including your file path in the variable of the same name.

# Financial Data Daily & Annualized Volatility Calculation (Task 2)

This repository contains a FastAPI-based web service for computing daily and annualized volatility from a CSV file with financial data.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [HTTP Endpoint](#http-endpoint)
- [Sample cURL Request](#sample-curl-request)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The python file is a web service that calculates daily and annualized volatility from a given financial dataset in CSV format. It uses FastAPI, a modern, fast & high-performance web framework for building APIs with Python 3.7+.

## Features

- **Daily and Annualized Volatility Calculation:** The service calculates daily returns, daily volatility, and annualized volatility based on a financial dataset.

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- [Pandas](https://pandas.pydata.org/): A fast, powerful, and flexible open-source data analysis and manipulation library for Python.
- [NumPy](https://numpy.org/): A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with mathematical functions to operate on these elements.
- [uvicorn](https://www.uvicorn.org/): A lightning-fast ASGI server, implementing the ASGI specification.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ojas21/Finzome_Assignments.git
   cd Finzome_Assignment
## Usage
1. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
2. Open the FastAPI documentation in your browser:
    ```bash
   http://127.0.0.1:8000/docs

## HTTP Endpoint
   Endpoint: /compute_volatility
   Method: POST
   Parameters:
      file (type: file) - CSV file containing financial data.
      file_path (type: string) - Path to the CSV file (optional if using file upload).
## Sample cURL Request
```bash
   curl -X 'POST' \
     'http://127.0.0.1:8000/compute_volatility' \
     -H 'accept: application/json' \
     -H 'Content-Type: multipart/form-data' \
     -F 'file=@path/to/your/financial_data.csv;type=text/csv'
```
## License
   This project is licensed under the MIT License.


