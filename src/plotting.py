import plotly.express as px
import pandas as pd
import numpy as np
    
def construct_leg_payoff(
        type:str,
        position:str,
        K:float,
        price_range:np.array
    ) -> np.array:
    
    multiplier = 1 if position.upper() == "LONG" else -1

    if type.upper() == "CALL":
        return np.array([(lambda S: np.multiply(multiplier, max(S-K, 0)))(S) for S in price_range])
    elif type.upper() == "PUT":
        return np.array([(lambda S: np.multiply(multiplier, max(K-S, 0)))(S) for S in price_range])


def construct_net_payoff(legs:dict) -> pd.DataFrame:
    n_legs = len(legs["type"])
    price_range = np.arange(
        start=round(min(legs["strike"])*0.8), 
        stop=round(max(legs["strike"])*1.2),
        step=0.1
        )
    
    payoffs = pd.DataFrame(index=price_range)
    net_leg_cost = np.where([x.upper() == "LONG" for x in legs["position"]] , -1, 1) * np.multiply(legs["price"], legs["lot"])

    for i in range(n_legs):
        leg_type = legs["type"][i]
        position = legs["position"][i]
        strike = legs["strike"][i]

        payoffs[f"Leg {i+1}: {position} {leg_type}"] = construct_leg_payoff(
            leg_type,
            position,
            strike,
            price_range
            )
        
    return pd.DataFrame(payoffs + net_leg_cost)

def plot_profit_loss_diagram(legs:dict) -> None:
    pass
    
        


