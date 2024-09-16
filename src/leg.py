from datetime import date
import numpy as np

from tastytrade.instruments import Option

from .greeks import Greeks


class Leg:
    def __init__(
        self,
        underlying: str,
        contract_type: str,
        strike: float,
        lot_size: int,
        expiration: date,
    ):
        self.underlying = underlying
        self.contract_type = contract_type
        self.strike = strike
        self.lot_size = lot_size
        self.expiration = expiration
        self.dte = self.compute_dte()
        self.T = self.dte / 365
        self.occ_symbol = self.construct_occ_symbol()
        self.streamer_symbol = Option.occ_to_streamer_symbol(self.occ_symbol)
        self.theo_price = None
        self.greeks = None
        self.validity_check()

    def validity_check(self):
        if self.dte < 0:
            raise ValueError("Contract must have positive time to expiration.")
        if self.contract_type not in ["call", "put"]:
            raise ValueError("Contract type must be either 'call' or 'put'")

    def construct_occ_symbol(self):
        root = self.underlying.ljust(6)
        yy = str(self.expiration.year)[-2:]
        mm = str(self.expiration.month).rjust(2, "0")
        dd = str(self.expiration.day).rjust(2, "0")
        option_type = self.contract_type[0].upper()
        strike = str(int(self.strike * 1000)).rjust(8, "0")

        return f"{root}{yy}{mm}{dd}{option_type}{strike}"

    def compute_dte(self):
        return int(
            np.ceil(((self.expiration - date.today()).total_seconds() / (24 * 60 * 60)))
        )

    def describe(self):
        return vars(self)
