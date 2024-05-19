import pandas as pd
from yahooquery import Ticker

def pull_history(
        ticker:Ticker,
        **kwargs
        ) -> pd.DataFrame:
        return ticker.history(**kwargs)