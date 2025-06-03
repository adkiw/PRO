# tables/kroviniai.py
import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_kroviniai_table(rows: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Display cargo table with dynamic editing enabled.
    Returns the edited DataFrame for processing.
    """
    if not rows:
        st.info("ℹ️ No cargo records.")
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    # Saugumo sumetimais konvertuojame į string
    df['id'] = df['id'].astype(int)
    df['busena'] = df['busena'].astype('category')

    edited_df = st.experimental_data_editor(
        df,
        key="kroviniai_editor",
        num_rows="dynamic",
        use_container_width=True
    )
    return edited_df
