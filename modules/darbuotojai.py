import streamlit as st
import pandas as pd

from forms.darbuotojai import darbuotojas_form as darbuotojai_form
from logic.darbuotojai import get_all_darbuotojai, insert_darbuotojas, update_grupe
from table.darbuotojai import show_darbuotojai_table as darbuotojai_table

def show(conn, c):
    st.title("DISPO – Employees")

    with st.expander("➕ Add new employee", expanded=True):
        data = darbuotojai_form(conn, c)
        if data and st.button("💾 Save employee"):
            insert_darbuotojas(conn, c, data)
            st.success("✅ Employee saved")

    df = pd.DataFrame(
        get_all_darbuotojai(conn, c),
        columns=["id", "vardas", "pavarde", "pareigybe",
                 "el_pastas", "telefonas", "grupe"]
    )
    edited = darbuotojai_table(df, key="darbuotojai")

    if edited is not None:
        for row in edited.to_dict(orient="records"):
            update_grupe(conn, c, row["id"], row["grupe"])
        st.success("✅ Groups updated")
