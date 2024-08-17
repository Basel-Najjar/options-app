from datetime import datetime
import numpy as np
from .greeks import GreeksDict, GreeksObject


class Leg:
    def __init__(
        self,
        contract_type: str,
        strike: float,
        contract_price: float,
        iv: float,
        greeks: GreeksDict,
        lot_size: int,
        expiration: datetime,
    ):

        self.contract_type = contract_type
        self.strike = strike
        self.contract_price = contract_price
        self.iv = iv
        self.lot_size = lot_size
        self.expiration = expiration
        self.dte = self.compute_dte()

        scaled_greeks = self.scale_greeks(greeks)
        self.greeks = GreeksObject(scaled_greeks)
        self.type_check()

    def type_check(self):
        if self.dte < 0:
            raise ValueError("Contract must have positive time to expiration.")
        if self.contract_type not in ["call", "put"]:
            raise ValueError("Contract type must be either 'call' or 'put'")

    def compute_dte(self):
        return int(
            np.ceil(
                ((self.expiration - datetime.today()).total_seconds() / (24 * 60 * 60))
            )
        )

    def scale_greeks(self, greeks: GreeksDict) -> GreeksDict:
        return {key: value * self.lot_size for key, value in greeks.items()}

    def describe(self):
        return vars(self)
