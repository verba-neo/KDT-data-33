# browse.py
import webbrowser

tickers = [
    'NVDA:NASDAQ',
    'AAPL:NASDAQ',
    'TSLA:BMV',
    '005930:KRX',
    '035420:KRX',
    'GOOGL:NASDAQ',
]

for tick in tickers:
    url = 'https://www.google.com/finance/quote/' + tick
    webbrowser.open(url)
