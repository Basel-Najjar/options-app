import pandas as pd


TODAY = pd.Timestamp('now').floor('d')
REQUEST_LIMIT = 1000
MARKET = 'stocks'