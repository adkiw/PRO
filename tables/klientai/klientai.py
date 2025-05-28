# tables/klientai.py
import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_klientai_table(rows: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Rodo klientų lentelę su galimybe redaguoti įrašus dinamškai.
    Grąžina redaguotą DataFrame.
    """
    if not rows:
        st.info("ℹ️ Nėra klientų įrašų.")
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    # Konvertuojame stulpelius tinkamoms kategorijoms
    df['id'] = df['id'].astype(int)
    edited_df = st.experimental_data_editor(
        df,
        key="klientai_editor",
        num_rows="dynamic",
        use_container_width=True
    )
    return edited_df
