import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Define the dictionary with companies and cryptocurrencies
companies = {
    'AAPL': 'Apple Inc.',
    'MSFT': 'Microsoft Corporation',
    'GOOGL': 'Alphabet Inc. (Google)',
    'FB': 'Meta Platforms, Inc. (Facebook)',
    'AMZN': 'Amazon.com, Inc.',
    'TSLA': 'Tesla, Inc.',
    'NVDA': 'Nvidia Corporation',
    'INTC': 'Intel Corporation',
    'AMD': 'Advanced Micro Devices, Inc.',
    'ADBE': 'Adobe Inc.',
    'CRM': 'Salesforce.com, Inc.',
    'CSCO': 'Cisco Systems, Inc.',
    'WMT': 'Walmart Inc.',
    'KO': 'The Coca-Cola Company',
    'PEP': 'PepsiCo, Inc.',
    'PG': 'Procter & Gamble Co.',
    'HD': 'The Home Depot, Inc.',
    'MCD': "McDonald's Corporation",
    'NKE': 'Nike, Inc.',
    'TGT': 'Target Corporation',
    'COST': 'Costco Wholesale Corporation',
    'CL': 'Colgate-Palmolive Company',
    'DIS': 'The Walt Disney Company',
    'NFLX': 'Netflix, Inc.',
    'CMCSA': 'Comcast Corporation',
    'SPOT': 'Spotify Technology S.A.',
    'VIAC': 'ViacomCBS Inc.',
    'ATVI': 'Activision Blizzard, Inc.',
    'EA': 'Electronic Arts Inc.',
    'JPM': 'JPMorgan Chase & Co.',
    'BAC': 'Bank of America Corporation',
    'V': 'Visa Inc.',
    'MA': 'Mastercard Incorporated',
    'PYPL': 'PayPal Holdings, Inc.',
    'BRK.B': 'Berkshire Hathaway Inc.',
    'JNJ': 'Johnson & Johnson',
    'PFE': 'Pfizer Inc.',
    'MRK': 'Merck & Co., Inc.',
    'ABBV': 'AbbVie Inc.',
    'BMY': 'Bristol-Myers Squibb Company',
    'UNH': 'UnitedHealth Group Incorporated',
    'XOM': 'Exxon Mobil Corporation',
    'CVX': 'Chevron Corporation',
    'BP': 'BP p.l.c.',
    'RDS-A': 'Royal Dutch Shell plc',
    'VZ': 'Verizon Communications Inc.',
    'T': 'AT&T Inc.',
    'F': 'Ford Motor Company',
    'GM': 'General Motors Company',
    'TM': 'Toyota Motor Corporation',
    'HMC': 'Honda Motor Co., Ltd.',
    'BA': 'The Boeing Company',
    'LMT': 'Lockheed Martin Corporation',
    'RTX': 'Raytheon Technologies Corporation',
    'NEE': 'NextEra Energy, Inc.',
    'DUK': 'Duke Energy Corporation',
    'SO': 'Southern Company',
    'AMT': 'American Tower Corporation',
    'SPG': 'Simon Property Group, Inc.',
    'SHW': 'The Sherwin-Williams Company',
    'DOW': 'Dow Inc.',
    'FCX': 'Freeport-McMoRan Inc.',
    'BTC-USD': 'Bitcoin (BTC)',
    'ETH-USD': 'Ethereum (ETH)',
    'BNB-USD': 'Binance Coin (BNB)',
    'ADA-USD': 'Cardano (ADA)',
    'XRP-USD': 'Ripple (XRP)',
    'DOGE-USD': 'Dogecoin (DOGE)',
    'DOT1-USD': 'Polkadot (DOT)',
    'SOL1-USD': 'Solana (SOL)',
    'UNI3-USD': 'Uniswap (UNI)',
    'LINK-USD': 'Chainlink (LINK)'
}

def find_high_correlation_stocks(symbol, threshold=0.8, date_time=None):
    try:
        # Calculate start and end dates for the previous month from the given date_time
        if date_time is None:
            date_time = datetime.now()
        
        end_date = date_time
        start_date = end_date - timedelta(days=30)
        
        # Format dates for yfinance
        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date_str = end_date.strftime('%Y-%m-%d')
        
        # Fetch historical data for the given symbol
        stock_data = yf.download(symbol, start=start_date_str, end=end_date_str)['Adj Close']
        
        # Fetch historical data for all symbols
        all_symbols = list(companies.keys())
        all_data = yf.download(all_symbols, start=start_date_str, end=end_date_str)['Adj Close']
        
        # Calculate correlations with the given symbol
        correlations = all_data.corrwith(stock_data, axis=0).sort_values(ascending=False)
        
        # Remove the given symbol from the list (since correlation with itself is 1.0)
        correlations = correlations.drop(symbol)
        
        # Filter correlations above the threshold
        relevant_correlations = correlations[correlations.abs() >= threshold]
        
        # Get names corresponding to the symbols
        relevant_names = relevant_correlations.index.map(companies)
        
        # Create DataFrame for better readability
        result_df = pd.DataFrame({
            'Symbol': relevant_correlations.index,
            'Name': relevant_names,
            'Correlation': relevant_correlations.values
        })
        
        return result_df
    
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    stock_symbol = 'AAPL'
    stock_symbol = 'BTC-USD'
    
    correlation_threshold = 0.8  # Example threshold, adjust as needed
    specific_date_time = datetime(2023, 1, 15, 12, 0, 0)  # Example specific date and time
    
    relevant_correlations = find_high_correlation_stocks(stock_symbol, threshold=correlation_threshold, date_time=specific_date_time)
    
    if relevant_correlations is not None:
        print(f"Stocks/Cryptocurrencies with correlation above {correlation_threshold} with {stock_symbol} as of {specific_date_time}:")
        print(relevant_correlations)
