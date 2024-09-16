from tastytrade.dxfeed import EventType
from decimal import Decimal


class Greeks:
    def __init__(self, greeks: EventType.GREEKS):
        greeks_dict = greeks.dict()
        for key, value in greeks_dict.items():
            if type(value) is Decimal:
                value = float(value)
            setattr(self, key, value)
