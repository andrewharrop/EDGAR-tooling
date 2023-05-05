import requests
import json

tmap = json.load(open('tickers_mapped.json', 'r'))

def update():
    tickers = json.load(open('tickers.json', 'r'))

    tmp_tickers = {}

    for t in tickers:
        # Get length of ticker
        ticker_str = str(tickers[t]['cik_str'])
        ticker_len = len(ticker_str)
        # Fill in leading zeros up to 10 characters
        ticker_str = '0'*(10-ticker_len) + ticker_str
        tmp_tickers[tickers[t]["ticker"]] = ticker_str

    # Write to file
    with open('tickers_mapped.json', 'w') as f:
        json.dump(tmp_tickers, f, indent=4)

def ticker_mapper(ticker:str):
    # Load tickers

    # Return CIK if ticker is found
    if ticker in tmap:
        return tmap[ticker]
    else:
        return None