import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_nustatymai_table(rows: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Rodo lookup reikšmių lentelę su galimybe redaguoti.
    rows turi būti sąrašas žodynų su laukais: id, kategorija, reiksme.
    Grąžina redaguotą DataFrame.
    """
    if not rows:
        st.info("ℹ️ Nėra reikšmių.")
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
