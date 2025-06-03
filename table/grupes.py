import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_grupes_table(rows: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Display groups table with editable number, name and description.
    Returns the edited DataFrame.
    """
    if not rows:
        st.info("ℹ️ No groups created.")
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    df['id'] = df['id'].astype(int)

    edited_df = st.experimental_data_editor(
        df,
        key="grupes_editor",
        num_rows="dynamic",
        use_container_width=True
    )
    return edited_df
