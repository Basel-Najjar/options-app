import streamlit as st
import pandas as pd
import numpy as np

from src.constants import *
from src.manual_legs import Leg, add_leg, remove_leg
from src.app_utils import *

if __name__ == "__main__":
    tab1, tab2 = st.tabs([MANUAL_LEGS_TAB_NAME, "TBD"])
    with tab1:
        st.header(MANUAL_LEGS_TAB_NAME)
        if 'legs' not in st.session_state:
            st.session_state.legs = []
            add_leg()
        head_col1, head_col2 = st.columns(2)
        with head_col1:
            st.button(
                "Add leg", 
                on_click=add_leg,
                )
        with head_col2:
            st.button(
                "Reset",
                on_click=reset_page
            )
        
        for leg in st.session_state.legs:
            leg.construct_leg()

