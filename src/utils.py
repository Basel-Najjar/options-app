import numpy as np


def generate_range(
    base_value: float,
    percentage_range: float = 0.05,
    # step_size: float = 0.05,
    # precision: int = 2,
    time: bool = False,
) -> np.ndarray:
    min_value = 0 if time else base_value * (1 - percentage_range)
    max_value = base_value if time else base_value * (1 + percentage_range)

    # return np.arange(min_value, max_value, step_size)
    if time:
        return np.linspace(min_value, max_value, num=50)[::-1]
    return np.linspace(min_value, max_value, num=50)


def simulate_contract_value_using_greeks(
    v0: float,
    x0: float,
    x_range: np.array,
    greek1: float,
    greek2: None | float = None,
    theta: bool = False,
) -> np.array:
    dx = (x0 - x_range) if theta else (x_range - x0)

    # Assume constant 2nd-order greek
    if greek2 is not None:
        greek1_adj = greek1 + dx * greek2
        return v0 + dx * greek1_adj

    # If no 2nd-order greek available, assume constant 1st-order greek
    return v0 + dx * greek1
