import numpy as np


def generate_price_range(
    base_value: float,
    percentage_range: float = 0.25,
    # step_size: float = 0.05,
    # precision: int = 2,
) -> np.array:
    min_value = base_value * (1 - percentage_range)
    max_value = base_value * (1 + percentage_range)
    return np.linspace(min_value, max_value, num=50)


def mid_price(bid: float, ask: float) -> float:
    return (bid + ask) / 2
