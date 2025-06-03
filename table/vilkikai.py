import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_vilkikai_table(rows: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Display trucks table with editing enabled.
    Returns the edited DataFrame.
    """
    if not rows:
        st.info("ℹ️ No trucks available.")
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    df['id'] = df['id'].astype(int)
    edited = st.experimental_data_editor(
        df,
        key="vilkikai_editor",
        num_rows="dynamic",
        use_container_width=True
    )
    return edited
