class StrategyMetrics:
    def __init__(self, net_greeks, net_value, net_theo_price, net_iv, min_dte):
        self.net_greeks = net_greeks
        self.net_value = net_value
        self.net_theo_price = net_theo_price
        self.net_iv = net_iv
        self.min_dte = min_dte
