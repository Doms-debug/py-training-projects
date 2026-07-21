# Asset price monitor

A CLI utility that fetches and displays live asset prices using the yfinance library. It features a continuous monitoring mode that automatically clears the terminal and refreshes the data at a specified interval

## Features

* Fetches real-time price data for stocks, ETFs, and cryptocurrencies
* Accepts multiple ticker symbols simultaneously
* Continuously refreshes data in the terminal
* Allows custom refresh intervals via command-line arguments
* Handles graceful exits via keyboard interrupt (CTRL+C)

## Setup and installation

* Navigate to the project directory
* Create a virtual environment using `python -m venv venv`
* Activate the virtual environment
* Install the required dependencies using `pip install -r requirements.txt` (requires `yfinance`)

### Usage

Run the script from the terminal, passing one or more ticker symbols as arguments.

```
# Monitor multiple assets with the default 10-second interval
python monitor.py AAPL MSFT TSLA

# Monitor assets with a custom 3-second refresh interval
python monitor.py BTC-USD NVDA --interval 3

```

### Sample output

```
--- Live asset prices ---
Refreshing every 3 seconds. Press Ctrl+C to stop

BTC-USD: 66338.0 USD
AAPL: 327.74 USD
NVDA: 207.29 USD
```