from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np

"""
    this program computes Daily and Annualized Volatility from a CSV file.
    Parameters:
    - file: UploadFile - CSV file uploaded using form data.
    Returns:
    - JSONResponse: JSON with computed Daily and Annualized Volatility.
"""

app = FastAPI()

@app.post("/compute_volatility")
async def compute_volatility(file: UploadFile = File(None), file_path: str = None):
    

    # Read data from either file upload or specified file path
    if file:
        df = pd.read_csv(file.file)
    elif file_path:
        df = pd.read_csv(file_path)
    else:
        raise HTTPException(status_code=400, detail="Either file or file_path must be provided.")

    # Adjust column names if needed
    df.columns = df.columns.str.strip().str.replace(' ', '_', regex=True)

    # Print columns for debugging
    print("Columns in the DataFrame:", df.columns)

    # Validate the presence of necessary columns
    required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Shares_Traded', 'Turnover_(â‚¹_Cr)']

    if not set(required_columns).issubset(df.columns):
        raise HTTPException(status_code=400, detail="Required columns are missing in the CSV file.")

    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y', dayfirst=True)
    #Calculating daily returns
    
    #for testing purposes
    #current_close = 18107.85
    #previous_close = 18165.35
    #daily_returns = (current_close / previous_close) - 1
    #print("Daily Returns:", daily_returns)
    #answer= -0.003165
    
    df['Daily_Returns'] = df['Close'] / df['Close'].shift(1) - 1

    # Calculates Daily Volatility
    daily_volatility = df['Daily_Returns'].std()

    # Calculating Annualized Volatility
    length_of_data = len(df)
    annualized_volatility = daily_volatility * np.sqrt(length_of_data)

    # Returning the computed values
    result = {"Daily_Volatility": daily_volatility, "Annualized_Volatility": annualized_volatility}
    return JSONResponse(content=result)
