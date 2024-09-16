import yfinance as yf
from tastytrade import DXLinkStreamer
from tastytrade.dxfeed import EventType
from .utils import *


def get_current_stock_price(ticker: str) -> float:
    stock = yf.Ticker(ticker)
    return mid_price(stock.info["bid"], stock.info["ask"])


async def get_greeks(session, symbols: list[str]) -> EventType.GREEKS:
    greek_stream = []
    async with DXLinkStreamer(session) as streamer:
        # Ensure we are subscribing to a list of symbols
        await streamer.subscribe(EventType.GREEKS, symbols)

        # Listen for Greek events and collect them
        async for greeks in streamer.listen(EventType.GREEKS):
            greek_stream.append(greeks)

            if len(greek_stream) >= len(symbols):
                return greek_stream
