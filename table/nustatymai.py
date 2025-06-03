import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_nustatymai_table(rows: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Display lookup values table with editing enabled.
    Rows should be dicts with: id, kategorija, reiksme.
    Returns the edited DataFrame.
    """
    if not rows:
        st.info("ℹ️ No values found.")
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    df['id'] = df['id'].astype(int)
    # kad būtų aišku, kokia kategorija ir reikšmė
    edited_df = st.experimental_data_editor(
        df,
        key="nustatymai_editor",
        num_rows="dynamic",
        use_container_width=True
    )
    return edited_df
