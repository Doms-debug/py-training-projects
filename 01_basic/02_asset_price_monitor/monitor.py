import argparse
import time
import os
import yfinance as yf

def get_price(symbol):
    """Fetches the current price for a single ticker symbol"""
    try:
        ticker = yf.Ticker(symbol)
        price = ticker.fast_info['lastPrice']
        return round(price, 2)
    except Exception:
        return None

def main():
    parser = argparse.ArgumentParser(description="Live asset price monitoring")
    parser.add_argument("symbols", nargs='+', help="Stock tickers (like AAPL, MSFT, TSLA")
    # arg to control the refresh rate
    parser.add_argument("--interval", type=int, default=10, help="Refresh interval in seconds (default: 10)")
    
    args = parser.parse_args()
    
    try:
        while True:
            # clear terminal screen
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("--- Live asset prices ---")
            print(f"Refreshing every {args.interval} seconds. Press Ctrl+C to stop\n")
            
            for symbol in args.symbols:
                symbol = symbol.upper() 
                price = get_price(symbol)
                
                if price is not None:
                    print(f"{symbol}: {price} USD")
                else:
                    print(f"{symbol}: Error - symbol not found")
                    
            # pause execution
            time.sleep(args.interval)
            
    except KeyboardInterrupt:
        # graceful exit 
        print("\nMonitoring stopped by user")

if __name__ == "__main__":
    main()