# from typing import TypedDict
from tastytrade.dxfeed import EventType
from decimal import Decimal


class Greeks:
    def __init__(self, greeks: EventType.GREEKS):
        greeks_dict = greeks.dict()
        for key, value in greeks_dict.items():
            if type(value) is Decimal:
                value = float(value)
            setattr(self, key, value)


# class GreeksObject:
#     def __init__(self, greeks: GreeksDict):

#         self.delta = float(greeks["delta"])
#         self.gamma = float(greeks["gamma"])
#         self.theta = float(greeks["theta"])
#         self.vega = float(greeks["vega"])

#     def describe(self):
#         return vars(self)
