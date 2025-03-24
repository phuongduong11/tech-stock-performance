# 📈 Stock Price Analysis - Yahoo Finance API

## Project Purpose

This project analyzes the stock performance of five major technology companies — **Amazon, Meta, Alphabet, Microsoft, and Apple** — throughout **2023**. Using the **Yahoo Finance API**, it retrieves historical stock data and calculates key performance metrics including **average/max closing prices, daily returns, volatility, and moving averages**.


## Dataset Description

The dataset contains daily trading data for each stock with the following columns:
- `Date`: Trading date
- `Open`, `High`, `Low`, `Close`: Daily stock price metrics
- `Adj Close`: Adjusted close price
- `Volume`: Total shares traded
- `Ticker`, `Company`: Identifier and company name

## Methodology

### 1️⃣ Data Collection
- Utilized `yfinance` to fetch data from **January 1, 2023** to **December 31, 2023**
- Stocks analyzed:
  - `AMZN` – Amazon
  - `META` – Meta
  - `GOOG` – Alphabet
  - `MSFT` – Microsoft
  - `AAPL` – Apple
- Combined into one DataFrame for unified analysis

### 2️⃣ Data Analysis
- **Average Closing Price** per company
- **Maximum Closing Price** during the year
- **Daily Returns (%)** using `pct_change()`
- **Best/Worst Return Days** per stock
- **Standard Deviation of Returns** to assess risk
- **Monthly Risk** – riskiest stock per month
- **Moving Averages** for trend smoothing

## 🔍 Key Insights
- **Average Closing Prices**: Provide a baseline view of each company’s stock valuation throughout 2023.
- **Best & Worst Return Days**: Highlight significant market reactions, earnings events, or macroeconomic influences.
- **Risk Assessment**: Quantifies the overall risk level and volatility of each stock.

## 🚀 Business Implications
- **Investor Asset Allocation**: Helps investors make informed decisions by identifying stocks with varying levels of risk and stability.
- **Performance Benchmarking**: Allows comparison of stock behaviors within the tech sector for smarter portfolio diversification.
- **Market Timing Signals**: Insights from best/worst return days and volatility trends can help inform more strategic entry and exit points.

## 🛠 Tools & Libraries

- **Python**
  - `yfinance` – Data extraction
  - `pandas` – Data wrangling & grouping
  - `numpy` – Return calculations
  - `datetime` – Time range creation and formatting
  - *(Optional: `matplotlib`, `seaborn`)* – For future visualizations

## Author
👩🏻‍💻 Phuong Duong  

