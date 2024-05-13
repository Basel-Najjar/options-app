import streamlit as st
import pandas as pd
from src.constants import *
from src.auth import auth

client = auth()

if __name__ == "__main__":

    col1, col2, col3 =  st.columns(3)
    with col1:
        ticker = st.text_input(
            label = 'Enter Symbol:').upper()

    #with col2:
    #    start_date = st.date_input(
    #        label = 'Start Date',
    #        value = TODAY - pd.Timedelta('90d')
    #    )
#
    #with col3:
    #    end_date = st.date_input(
    #        label = 'Start Date',
    #        value = TODAY
    #    )
    contract_names=list()
    for c in client.list_options_contracts(
        underlying_ticker=ticker,
        limit=1000
        ):
        contract_names.append(c)
    st.dataframe(pd.DataFrame(contract_names))
    


