# Finzome_Assignments
Solutions to the Task 1&amp;2 in the assigned Finzome Challenge

# Financial Data Volatility Calculation (Task 1)

This repository contains Python code for calculating daily and annualized volatility from a financial dataset. The dataset is expected to be in CSV format, and the calculations are performed using Python with the help of Pandas and NumPy libraries.

## Table of Contents
- [Introduction](#introduction)
- [Calculations](#calculations)
- [Tech Stack](#tech-stack)
- [Usage](#usage)
- [Sample Dataset](#sample-dataset)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The purpose of this project is to provide a Python script for calculating daily and annualized volatility from financial data. It uses standard financial formulas and leverages Pandas and NumPy for efficient data manipulation and calculations.

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
The sample dataset used for testing the script is available in the data directory. You can replace it with your own financial dataset.


