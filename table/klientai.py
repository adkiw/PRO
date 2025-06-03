import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_klientai_table(rows: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Display clients table with edit capability.
    Returns the edited DataFrame for processing.
    """
    if not rows:
        st.info("ℹ️ No client records.")
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    # Užtikriname, kad ID būtų int tipo
    df['id'] = df['id'].astype(int)

    # Leidžiame redaguoti (pvz. pavadinimą, kontaktus, miestą ir kt.)
    edited_df = st.experimental_data_editor(
        df,
        key="klientai_editor",
        num_rows="dynamic",
        use_container_width=True
    )
    return edited_df
