import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_darbuotojai_table(rows: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Rodo darbuotojų lentelę su galimybe redaguoti įrašus.
    Grąžina redaguotą DataFrame, kad būtų galima apdoroti pakeitimus.
    """
    if not rows:
        st.info("ℹ️ Nėra darbuotojų įrašų.")
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    df['id'] = df['id'].astype(int)

    edited_df = st.experimental_data_editor(
        df,
        key="darbuotojai_editor",
        num_rows="dynamic",
        use_container_width=True
    )
    return edited_df
