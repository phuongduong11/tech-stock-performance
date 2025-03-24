import yfinance as yf
import pandas as pd
import numpy as np
import datetime

# -------------------------------------
# Step 1: Download Stock Data
# -------------------------------------
start = datetime.datetime(2023, 1, 1)
end = datetime.datetime(2023, 12, 31)

tickers = {
    "Amazon": "AMZN",
    "Meta": "META",
    "Alphabet": "GOOG",
    "Microsoft": "MSFT",
    "Apple": "AAPL"
}

# Download and prepare data
all_data = pd.DataFrame()
for company, symbol in tickers.items():
    df = yf.download(symbol, start=start, end=end)
    df['Company'] = company
    df['Ticker'] = symbol
    all_data = pd.concat([all_data, df], ignore_index=True)

# -------------------------------------
# Step 2: Basic Descriptive Stats
# -------------------------------------

# Average closing price
avg_close = all_data.groupby("Ticker")["Close"].mean().reset_index(name="Avg_Close")
print("Average Closing Prices:\n", avg_close)

# Max closing price
max_close = all_data.groupby("Ticker")["Close"].max().reset_index(name="Max_Close")
print("\nMaximum Closing Prices:\n", max_close)

# -------------------------------------
# Step 3: Return Analysis
# -------------------------------------

# Calculate daily percentage returns
returns = all_data[["Date", "Ticker", "Close"]].copy()
returns["Returns"] = returns.groupby("Ticker")["Close"].pct_change()
returns.dropna(inplace=True)

# Identify best/worst return days per company
best_returns = returns.loc[returns.groupby("Ticker")["Returns"].idxmax()]
worst_returns = returns.loc[returns.groupby("Ticker")["Returns"].idxmin()]

print("\nBest Return Days:\n", best_returns[["Date", "Ticker", "Returns"]])
print("\nWorst Return Days:\n", worst_returns[["Date", "Ticker", "Returns"]])

# -------------------------------------
# Step 4: Risk Analysis (Standard Deviation)
# -------------------------------------

# Overall risk (standard deviation)
risk_std = returns.groupby("Ticker")["Returns"].std().reset_index(name="Std_Dev")
risk_std_sorted = risk_std.sort_values(by="Std_Dev", ascending=False)
print("\nStandard Deviation (Risk) per Stock:\n", risk_std_sorted)

# Monthly risk
returns["Month"] = pd.to_datetime(returns["Date"]).dt.to_period("M")
monthly_risk = returns.groupby(["Ticker", "Month"])["Returns"].std().reset_index(name="Std_Dev")
monthly_riskiest = monthly_risk.loc[monthly_risk.groupby("Month")["Std_Dev"].idxmax()]
print("\nRiskiest Stock Each Month:\n", monthly_riskiest)

# -------------------------------------
# Step 5: Moving Averages
# -------------------------------------

# Prepare and sort data
all_data["Date"] = pd.to_datetime(all_data["Date"])
all_data.sort_values(by=["Ticker", "Date"], inplace=True)

# Calculate 5-day moving average
all_data["MA_5"] = all_data.groupby("Ticker")["Close"].rolling(window=5).mean().reset_index(level=0, drop=True)
all_data.fillna(0, inplace=True)

# Preview with moving averages
print("\nSample Data with 5-day MA:\n", all_data.head())