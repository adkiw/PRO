import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_grupes_table(rows: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Rodo grupių lentelę su galimybe redaguoti:
    numerį, pavadinimą, aprašymą.
    Grąžina redaguotą DataFrame.
    """
    if not rows:
        st.info("ℹ️ Nėra sukurtų grupių.")
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
