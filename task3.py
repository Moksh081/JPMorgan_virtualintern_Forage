import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
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

# Create the Dash web application
app = dash.Dash(__name__)

# Define the layout of the web application
app.layout = html.Div(children=[
    html.H1(children='Trading Analysis Dashboard'),
    
    # Dash core component for displaying Perspective table
    dcc.Graph(id='live-update-graph'),

    # Interval component for updating the data every second
    dcc.Interval(
        id='interval-component',
        interval=1 * 1000,  # in milliseconds
        n_intervals=0
    )
])

# Callback function to update the Perspective table and graph
@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_layout(n_intervals):
    update_perspective_table()

    # Get the data from the Perspective table
    data = table.view().to_dict()

    # Create a scatter plot using the data
    figure = {
        'data': [
            {
                'x': data['Date'],
                'y': data['Price'],
                'type': 'scatter',
                'mode': 'lines+markers',
                'name': stock
            } for stock in set(data['Stock'])
        ],
        'layout': {
            'title': 'Stock Prices Over Time',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Stock Price'}
        }
    }

    return figure

# Run the Dash web application
if __name__ == '__main__':
    app.run_server(debug=True)
