import numpy as np
from scipy.stats import norm


def black_scholes_merton(
    S: float, K: float, T: float, r: float, sigma: float, contract_type: str = "call"
) -> np.array:
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if contract_type == "call":
        # Call option formula
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif contract_type == "put":
        # Put option formula
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Must be 'call' or 'put'.")
