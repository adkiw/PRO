import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_priekabos_table(rows: List[Dict[str, Any]]) -> pd.DataFrame:
    if not rows:
        st.info("ℹ️ Nėra priekabų.")
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    df['id'] = df['id'].astype(int)
    edited = st.experimental_data_editor(
        df,
        key="priekabos_editor",
        num_rows="dynamic",
        use_container_width=True
    )
    return edited
