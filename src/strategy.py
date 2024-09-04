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
        self.net_greeks, self.net_value, self.net_iv, self.min_dte = (
            self.compute_metrics()
        )

    def show_strategy(self):
        for idx, leg in enumerate(self.legs):
            print(
                f"Leg {idx + 1}: {leg['position']} {leg['type']} with strike {leg['strike']} at price {leg['contract_price']}"
            )

    def compute_metrics(self):
        net_greeks = GreeksDict(delta=0, gamma=0, theta=0, vega=0)
        net_value = 0
        net_iv = 0
        dte_list = list()

        for leg in self.legs:
            # Greeks calculation
            net_greeks["delta"] += leg.greeks.delta
            net_greeks["gamma"] += leg.greeks.gamma
            net_greeks["theta"] += leg.greeks.theta
            net_greeks["vega"] += leg.greeks.vega

            # Net value calculation
            net_value += leg.contract_price

            # Net IV calculation (weighted-delta approach)
            net_iv += (leg.iv * leg.greeks.delta) / leg.greeks.delta

            # Min DTE calculation
            dte_list.append(leg.dte)

        return GreeksObject(net_greeks), net_value, net_iv, min(dte_list)

    # def compute_net_greeks(self):
    #     net_greeks = GreeksDict(delta=0, gamma=0, theta=0, vega=0)

    #     for leg in self.legs:
    #         net_greeks["delta"] += leg.greeks.delta
    #         net_greeks["gamma"] += leg.greeks.gamma
    #         net_greeks["theta"] += leg.greeks.theta
    #         net_greeks["vega"] += leg.greeks.vega

    #     return GreeksObject(net_greeks)

    # def compute_net_value(self) -> float:
    #     net_value = 0
    #     for leg in self.legs:
    #         net_value += leg.contract_price
    #     return net_value

    # def compute_net_iv(self) -> float:
    #     net_iv = 0
    #     for leg in self.legs:
    #         net_iv += (leg.iv * leg.greeks.vega) / leg.iv
    #     return net_iv

    # def compute_near_dte(self) -> int:
    #     dte_list = list()
    #     for leg in self.legs:
    #         dte_list.append(leg.dte)
    #     return max(dte_list)

    def describe(self):
        attr = list()
        for leg in self.legs:
            attr_dict = leg.describe()
            attr_dict["greeks"] = leg.greeks.describe()
            attr.append(attr_dict)
        return attr
