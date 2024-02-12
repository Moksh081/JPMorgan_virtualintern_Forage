import pandas as pd
import random
import time
import perspective

# Create a Perspective table
table = perspective.Table({
    "Date": str,
    "Stock": str,
    "Price": float,
    "Volume": int
})

# Function to generate random data
def generate_random_data():
    stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
    return {
        "Date": [pd.Timestamp.now()] * len(stocks),
        "Stock": stocks,
        "Price": [round(random.uniform(100, 1500), 2) for _ in range(len(stocks))],
        "Volume": [random.randint(100000, 1000000) for _ in range(len(stocks))]
    }

# Function to update the Perspective table
def update_perspective_table():
    data = generate_random_data()
    table.update(data)
    time.sleep(1)

# Run the example
if __name__ == "__main__":
    # Create a Perspective client
    client = perspective.PerspectiveWidget([table])

    # Continuously update the Perspective table with random data
    while True:
        update_perspective_table()
