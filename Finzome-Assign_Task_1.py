import pandas as pd
import numpy as np

"""
    this program computes Daily return, Daily Volatility and Annualized Volatility from a CSV file.
    Parameters:
    - file_path - replace CSV file path with your local directory path
    Returns:
    - prints the Daily and Annualized Volatility
"""

# file path
file_path = 'C:\\path\\test.csv'

# reading data from the csv file
df = pd.read_csv(file_path)

# Adjusting the column names by removing extra spaces and special characters, to extract data without any issues
df.columns = df.columns.str.strip().str.replace(' ', '_', regex=True).str.replace('₹', '', regex=True).str.replace('\(','', regex=True).str.replace('\)','', regex=True)

# Checking the column names
print(df.columns)

# Used to Adjust the date column name(optional)
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y', dayfirst=True)

# Calculating Daily Returns
'''
for testing purposes
current_close = 18107.85
previous_close = 18165.35

daily_returns = (current_close / previous_close) - 1

print("Daily Returns:", daily_returns)
answer= -0.003165
'''
df['Daily_Returns'] = df['Close'] / df['Close'].shift(1) - 1

#print(df['Daily_Returns'])

# Calculating Daily Volatility
daily_volatility = df['Daily_Returns'].std()

# Calculating Annualized Volatility
length_of_data = len(df)
annualized_volatility = daily_volatility * np.sqrt(length_of_data)

print("Daily Volatility:", daily_volatility)
print("Annualized Volatility:", annualized_volatility)
