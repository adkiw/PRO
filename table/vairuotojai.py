import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_vairuotojai_table(rows: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Display drivers table with edit options.
    Returns the edited DataFrame for processing.
    """
    if not rows:
        st.info("ℹ️ No driver records.")
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    df['id'] = df['id'].astype(int)

    edited_df = st.experimental_data_editor(
        df,
        key="vairuotojai_editor",
        num_rows="dynamic",
        use_container_width=True
    )
    return edited_df
