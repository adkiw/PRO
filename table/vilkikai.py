import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_vilkikai_table(rows: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Rodo vilkikų lentelę su galimybe redaguoti.
    Grąžina DataFrame su pakeitimais.
    """
    if not rows:
        st.info("ℹ️ Nėra vilkikų.")
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
