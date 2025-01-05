import pandas as pd
import numpy as np
import yfinance as yf

def get_data(ticker, start, end):
    raw_data = yf.download(ticker, start=start, end=end)
    df = raw_data['Close'].to_frame().rename(columns={"Close":"Price"})
    return df

def get_logreturns(df, freq=None):
    if freq is not None:
        try:
            df["Price"] = df.resample(freq).mean()
            df["Log Returns"] = np.log(df["Price"]/(df["Price"].shift(1)))
            return df
        except Exception as e:
            print("Error: ", e)
    df["Log Returns"] = np.log(df["Price"]/(df["Price"].shift(1)))
    return df
