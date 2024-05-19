import streamlit as st
import pandas as pd
from src.constants import *
from yahooquery import Ticker
import plotly.graph_objects as go

if __name__ == "__main__":

    ticker_name = st.text_input(
        label = 'Enter Symbol:',
        placeholder='AAPL',
        key='ticker_input'
        ).upper()
    
    col1, col2 = st.columns(2)
    with col1:
        period = st.select_slider(
            label = 'Select period',
            options = PERIODS,
            value='1mo'
        )
    with col2:
        interval = st.select_slider(
            label= "Select interval",
            options = INTERVALS,
            value='1d'
        )

    ticker = Ticker(ticker_name)
    df = ticker.history(period=period, interval=interval).loc[ticker_name]

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
    st.plotly_chart(fig)
