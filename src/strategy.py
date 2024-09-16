from .leg import Leg
from .pricing import black_scholes_merton
from .market_data import get_current_stock_price, get_greeks
from .constants import *
from .greeks import Greeks

from datetime import datetime

from tastytrade.metrics import get_risk_free_rate
from tastytrade.instruments import Option


class OptionStrategy:
    def __init__(self, underlying: str, session):
        self.underlying = underlying.upper()
        self.s0 = get_current_stock_price(self.underlying)
        self.r = float(get_risk_free_rate(session))
        self.session = session
        self.legs = list()

    async def add_leg(
        self,
        contract_type: str,
        strike: float,
        # contract_price: float,
        # iv: float,
        # greeks: GreeksDict,
        lot_size: int,
        expiration: datetime,
    ):

        leg = Leg(
            underlying=self.underlying,
            contract_type=contract_type,
            strike=strike,
            lot_size=lot_size,
            expiration=expiration,
        )
        # leg.theo_price = self.compute_theoretical_leg_price(leg)
        greeks = await get_greeks(self.session, [leg.streamer_symbol])
        leg.greeks = Greeks(greeks[0])
        self.legs.append(leg)

        # metrics = self.compute_metrics()
        # self.metrics = metrics

    def compute_theoretical_leg_price(self, leg):
        return black_scholes_merton(
            self.s0, leg.strike, leg.T, self.r, leg.iv, leg.contract_type
        )

    # def compute_metrics(self):
    #     net_greeks = GreeksDict(delta=0, gamma=0, theta=0, vega=0)
    #     net_value = 0
    #     net_theo_price = 0
    #     net_iv = 0
    #     dte_list = list()

    #     for leg in self.legs:
    #         # Greeks calculation
    #         net_greeks["delta"] += leg.greeks.delta
    #         net_greeks["gamma"] += leg.greeks.gamma
    #         net_greeks["theta"] += leg.greeks.theta
    #         net_greeks["vega"] += leg.greeks.vega

    #         # Net value calculation
    #         net_value += leg.lot_size * leg.contract_price
    #         net_theo_price += leg.lot_size * leg.theo_price

    #         # Net IV calculation (weighted-delta approach)
    #         net_iv += (leg.iv * leg.greeks.delta) / leg.greeks.delta

    #         # Min DTE calculation
    #         dte_list.append(leg.dte)

    #     return StrategyMetrics(
    #         GreeksObject(net_greeks),
    #         net_value,
    #         net_theo_price,
    #         net_iv,
    #         min(dte_list),
    #     )

    def describe(self):
        attr = list()
        for leg in self.legs:
            attr_dict = leg.describe()
            attr_dict["greeks"] = leg.greeks.describe()
            attr.append(attr_dict)
        return attr
