from typing import TypedDict


class GreeksDict(TypedDict):
    delta: float
    gamma: float
    theta: float
    vega: float


class GreeksObject:
    def __init__(self, greeks: GreeksDict):

        self.delta = float(greeks["delta"])
        self.gamma = float(greeks["gamma"])
        self.theta = float(greeks["theta"])
        self.vega = float(greeks["vega"])

    def describe(self):
        return vars(self)
