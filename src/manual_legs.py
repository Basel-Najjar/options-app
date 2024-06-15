import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from src.constants import *

class Leg:
    def __init__(self, id:int):
        self.id = id

    def construct_leg(self):
        with st.expander(f"Leg {self.id}", expanded=True):
            with st.container():
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    self.leg_type = st.radio(
                        "Type",
                        options = ["Call", "Put"],
                        key=f"leg_type_{self.id}"
                        )
                with col2:
                    self.leg_position = st.radio(
                        "Position",
                        options = ["Long", "Short"],
                        key = f"leg_position_{self.id}"
                    )

                with col3:
                    self.strike = st.number_input(
                        label = "Strike",
                        min_value=0.0,
                        step=0.5,
                        key=f"leg_strike_{self.id}"
                    )

                with col4:
                    self.mid_price = st.number_input(
                        label = "Mid-Price",
                        min_value=0.0,
                        step=0.05,
                        key=f"leg_price_{self.id}"
                    )
            with st.container():
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    self.delta = st.number_input(
                        label="Δ",
                        help="Option Delta",
                        min_value=-1.0,
                        max_value=1.0,
                        step=0.1,
                        value=0.0
                    )
                with col2:
                    self.gamma = st.number_input(
                        label="Γ",
                        help="Option Gamma",
                        min_value=-1.0,
                        max_value=1.0,
                        step=0.05,
                        value=0.0
                    )
                with col3:
                    self.theta = st.number_input(
                        label="Θ",
                        help="Option Vega",
                        min_value=-1.0,
                        max_value=1.0,
                        step=0.05,
                        value=0.0
                    )
                with col4:
                    self.vega = st.number_input(
                        label="ν",
                        help="Option Vega",
                        min_value=-1.0,
                        max_value=1.0,
                        step=0.05,
                        value=0.0
                    )
            st.button("Remove", key=f"remove_leg_{self.id}", on_click=remove_leg, args=(self.id,))

def add_leg():
    if 'legs' not in st.session_state:
        st.session_state.legs = []

    new_leg_id = len(st.session_state.legs) + 1
    new_leg = Leg(new_leg_id)
    st.session_state.legs.append(new_leg)

def remove_leg(leg_id):
    st.session_state.legs = [leg for leg in st.session_state.legs if leg.id != leg_id]


