import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_trading_data(file_path):
    data = pd.read_csv(file_path, parse_dates=[0], index_col=0)
    return data

def calculate_correlation(trades1, trades2):
    return np.corrcoef(trades1, trades2)[0, 1]

def plot_correlation_chart(dates, correlation_values):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, correlation_values, label='Correlation')
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.title('Historical Correlation of Buy/Sell Activities')
    plt.xlabel('Date')
    plt.ylabel('Correlation')
    plt.legend()
    plt.show()

def main():
    # Replace 'test.csv' with the actual file name
    csv_file_path = 'test.csv'

    # Read trading data from CSV
    trading_data = read_trading_data(csv_file_path)

    # Assuming you have two stocks named 'Stock1' and 'Stock2'
    stock1_trades = trading_data[trading_data['name'] == 'Stock1']['how much?']
    stock2_trades = trading_data[trading_data['name'] == 'Stock2']['how much?']

    # Calculate historical correlation of buy/sell activities
    historical_correlation = []
    window_size = 20  # Adjust as needed
    for i in range(window_size, len(stock1_trades)):
        correlation = calculate_correlation(stock1_trades.iloc[i - window_size:i], stock2_trades.iloc[i - window_size:i])
        historical_correlation.append(correlation)

    # Plot the historical correlation chart
    plot_correlation_chart(trading_data.index[window_size:], historical_correlation)

if __name__ == "__main__":
    main()
