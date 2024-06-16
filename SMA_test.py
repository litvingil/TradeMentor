import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def simple_moving_average(data, window):
    return data.rolling(window=window, min_periods=1).mean()

def exponential_moving_average(data, span):
    return data.ewm(span=span, adjust=False).mean()

def crossover_signals(data, short_window, long_window, average_type='sma'):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    
    if average_type == 'sma':
        signals['short_mavg'] = simple_moving_average(data['value'], short_window)
        signals['long_mavg'] = simple_moving_average(data['value'], long_window)
    elif average_type == 'ema':
        signals['short_mavg'] = exponential_moving_average(data['value'], short_window)
        signals['long_mavg'] = exponential_moving_average(data['value'], long_window)

    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()
    return signals

def add_signal_columns(data, short_window=50, long_window=200):
    sma_signals = crossover_signals(data, short_window, long_window, 'sma')
    data['short_mavg'] = sma_signals['short_mavg']
    data['long_mavg'] = sma_signals['long_mavg']
    data['Golden Cross'] = np.where(sma_signals['positions'] == 1, False, None)
    data['Death Cross'] = np.where(sma_signals['positions'] == -1, True, None)
    return data

# # Fetch stock data
# ticker = 'CHKP'
# data = yf.download(ticker, start='2020-01-01', end='2023-01-01')
if __name__ == "__main__":
        
    from utils import get_data
    data = get_data()

    # Calculate signals for SMA and EMA
    sma_signals = crossover_signals(data, 50, 200, 'sma')
    # ema_signals = crossover_signals(data, 50, 200, 'ema')

    # Plotting
    plt.figure(figsize=(14, 7))
    plt.plot(data['value'], label='Closing Price', color='gray')
    plt.plot(sma_signals['short_mavg'], label='50-Day SMA', color='r')
    plt.plot(sma_signals['long_mavg'], label='200-Day SMA', color='blue')

    # Mark the Golden Crosses and Death Crosses
    plt.plot(sma_signals.loc[sma_signals['positions'] == 1].index, 
            sma_signals.short_mavg[sma_signals['positions'] == 1],
            '^', markersize=10, color='g', lw=0, label='Golden Cross')

    plt.plot(sma_signals.loc[sma_signals['positions'] == -1].index, 
            sma_signals.short_mavg[sma_signals['positions'] == -1],
            'v', markersize=10, color='k', lw=0, label='Death Cross')
    plt.title('Apple Stock Price and SMA Crossover Signals')
    plt.legend()
    plt.show()
