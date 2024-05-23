import plotly.graph_objects as go
import pandas as pd

def plot_candles(df) -> None:
    fig = go.Figure(
        data = [
            go.Candlestick(
                x=df.index,
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close']
                )
        ]
    )
    fig.show()