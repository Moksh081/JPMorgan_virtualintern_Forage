import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Adj Close']

def calculate_returns(prices):
    return prices.pct_change().dropna()

def calculate_correlation(returns1, returns2):
    return np.corrcoef(returns1, returns2)[0, 1]

def plot_correlation_chart(dates, correlation_values):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, correlation_values, label='Correlation')
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.title('Historical Correlation')
    plt.xlabel('Date')
    plt.ylabel('Correlation')
    plt.legend()
    plt.show()

def main():
    # Example stock tickers and date range
    stock_ticker1 = 'AAPL'
    stock_ticker2 = 'MSFT'
    start_date = '2022-01-01'
    end_date = '2022-12-31'

    # Fetch historical stock prices
    stock1_prices = fetch_stock_data(stock_ticker1, start_date, end_date)
    stock2_prices = fetch_stock_data(stock_ticker2, start_date, end_date)

    # Calculate daily returns
    returns1 = calculate_returns(stock1_prices)
    returns2 = calculate_returns(stock2_prices)

    # Calculate historical correlation
    historical_correlation = []
    window_size = 20  # Adjust as needed
    for i in range(window_size, len(returns1)):
        correlation = calculate_correlation(returns1[i - window_size:i], returns2[i - window_size:i])
        historical_correlation.append(correlation)

    # Plot the historical correlation chart
    plot_correlation_chart(stock1_prices.index[window_size:], historical_correlation)

if __name__ == "__main__":
    main()
