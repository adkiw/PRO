# tables/kroviniai.py
import streamlit as st
import pandas as pd
from typing import List, Dict, Any

def show_kroviniai_table(rows: List[Dict[str, Any]]):
    """
    Rodo krovinių lentelę su galimybe redaguoti būseną tiesiogiai.
    """
    if not rows:
        st.info("Nėra krovinių įrašų.")
        return
    df = pd.DataFrame(rows)
    # Leidžiame redaguoti būseną
    df['busena'] = df['busena'].astype('category')
    edited = st.experimental_data_editor(
        df,
        num_rows="dynamic",
        use_container_width=True
    )
    # Grąžiname redaguotus duomenis, jei reikia toliau apdoroti
    return edited
