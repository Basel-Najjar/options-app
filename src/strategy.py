from .leg import Leg
from .greeks import GreeksDict, GreeksObject
from datetime import datetime


class OptionStrategy:
    def __init__(self, underlying: str, s0: float, r: float):
        self.underlying = underlying.upper()
        self.s0 = s0
        self.r = r
        self.legs = list()

    def add_leg(
        self,
        contract_type: str,
        strike: float,
        contract_price: float,
        iv: float,
        greeks: GreeksDict,
        lot_size: int,
        expiration: datetime,
    ):

        leg = Leg(
            contract_type=contract_type,
            strike=strike,
            contract_price=contract_price,
            iv=iv,
            greeks=greeks,
            lot_size=lot_size,
            expiration=expiration,
        )
        self.legs.append(leg)

        self.net_greeks = self.compute_net_greeks()
        self.net_value = self.compute_net_value()

    def show_strategy(self):
        for idx, leg in enumerate(self.legs):
            print(
                f"Leg {idx + 1}: {leg['position']} {leg['type']} with strike {leg['strike']} at price {leg['contract_price']}"
            )

    def compute_net_greeks(self):
        net_greeks = GreeksDict(delta=0, gamma=0, theta=0, vega=0)

        for leg in self.legs:
            net_greeks["delta"] += leg.greeks.delta
            net_greeks["gamma"] += leg.greeks.gamma
            net_greeks["theta"] += leg.greeks.theta
            net_greeks["vega"] += leg.greeks.vega

        return GreeksObject(net_greeks)

    def compute_net_value(self):
        net_value = 0
        for leg in self.legs:
            net_value += leg.contract_price
        return net_value

    def describe(self):
        attr = list()
        for leg in self.legs:
            attr_dict = leg.describe()
            attr_dict["greeks"] = leg.greeks.describe()
            attr.append(attr_dict)
        return attr
