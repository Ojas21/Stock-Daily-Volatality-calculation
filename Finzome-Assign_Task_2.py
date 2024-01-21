from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np

app = FastAPI()

@app.post("/compute_volatility")
async def compute_volatility(file: UploadFile = File(None), file_path: str = None):
    """
    Computes Daily and Annualized Volatility from a CSV file or a provided file path.

    Parameters:
    - file: UploadFile - CSV file uploaded using form data.
    - file_path: str - Optional. Path to the CSV file if not provided through file upload.

    Returns:
    - JSONResponse: JSON with computed Daily and Annualized Volatility.
    """

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

    # Calculate Daily Returns
    df['Daily_Returns'] = df['Close'].pct_change()

    # Calculate Daily Volatility
    daily_volatility = df['Daily_Returns'].std()

    # Calculate Annualized Volatility
    length_of_data = len(df)
    annualized_volatility = daily_volatility * np.sqrt(length_of_data)

    # Return the computed values
    result = {"Daily_Volatility": daily_volatility, "Annualized_Volatility": annualized_volatility}
    return JSONResponse(content=result)
