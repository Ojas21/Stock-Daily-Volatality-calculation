import pandas as pd
import numpy as np

# Read data from Excel file
file_path = 'C:\\path\\test.csv'

df = pd.read_csv(file_path)

# Adjust column names by removing extra spaces and special characters
df.columns = df.columns.str.strip().str.replace(' ', '_', regex=True).str.replace('₹', '', regex=True).str.replace('\(','', regex=True).str.replace('\)','', regex=True)

# Check column names
print(df.columns)

# Adjust date column name if needed
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y', dayfirst=True)

# Handle missing values if needed
# df = df.fillna(0)  # Replace NaN with 0 or use other appropriate methods

# Calculate Daily Returns
df['Daily_Returns'] = df['Close'].pct_change()

# Calculate Daily Volatility
daily_volatility = df['Daily_Returns'].std()

# Calculate Annualized Volatility
length_of_data = len(df)
annualized_volatility = daily_volatility * np.sqrt(length_of_data)

print("Daily Volatility:", daily_volatility)
print("Annualized Volatility:", annualized_volatility)
