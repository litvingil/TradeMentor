import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_rsi(data, window=14):
    """Calculate the Relative Strength Index (RSI) for given price data."""
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)

    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def detect_divergences(data, rsi):
    """Detect divergences between price and RSI."""
    # Calculating differences and rolling mean for trend analysis
    price_trend = data['Adj Close'].diff().rolling(window=14).mean()
    rsi_trend = rsi.diff().rolling(window=14).mean()

    # Identify potential divergences
    bullish_divergence = (price_trend < 0) & (rsi_trend > 0)
    bearish_divergence = (price_trend > 0) & (rsi_trend < 0)

    # Mapping the identified divergences back to the data DataFrame
    data['Bullish Divergence'] = bullish_divergence
    data['Bearish Divergence'] = bearish_divergence
    return data


# Download historical data for Apple Inc. from Yahoo Finance
data = yf.download("AAPL", start="2020-01-01", end="2023-01-01")
import pdb; pdb.set_trace()
prices = data['Adj Close']

# Calculate RSI
rsi = calculate_rsi(prices)

# Detect Divergences
data = detect_divergences(data, rsi)

#  the plotting section to handle boolean indexing correctly
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
ax1.plot(data.index, data['Adj Close'], label='Adjusted Close')
ax1.plot(data.index[data['Bullish Divergence']], data['Adj Close'][data['Bullish Divergence']], 'ro', markersize=5, label='Bullish Divergence')
ax1.plot(data.index[data['Bearish Divergence']], data['Adj Close'][data['Bearish Divergence']], 'go', markersize=5, label='Bearish Divergence')
ax1.set_title('Apple Inc. Stock Price and Divergences')
ax1.set_ylabel('Price ($)')
ax1.legend()

ax2.plot(data.index, rsi, label='RSI')
ax2.axhline(70, color='r', linestyle='--', linewidth=0.5, label='Overbought (70)')
ax2.axhline(30, color='g', linestyle='--', linewidth=0.5, label='Oversold (30)')
ax2.set_title('Relative Strength Index (RSI)')
ax2.set_ylabel('RSI Value')
ax2.legend()

plt.show()