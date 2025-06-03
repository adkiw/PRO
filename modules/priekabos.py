import streamlit as st
import pandas as pd

from forms.priekabos import priekaba_form as priekabos_form
from logic.priekabos import get_all_priekabos, insert_priekaba, update_priskirta
from table.priekabos import show_priekabos_table as priekabos_table

def show(conn, c):
    st.title("DISPO – Trailer Management")

    # 1. Input form
    with st.expander("➕ Add new trailer", expanded=True):
        data = priekabos_form(conn, c)
        if data and st.button("💾 Save trailer"):
            insert_priekaba(conn, c, data)
            st.success("✅ Trailer saved")

    # 2. Table
    df = pd.DataFrame(
        get_all_priekabos(conn, c),
        columns=["id", "tipas", "numeris", "marke",
                 "pagaminimo_metai", "tech_apziura", "priskirtas_vilkikas"]
    )
    edited = priekabos_table(df, key="priekabos")

    # 3. Update assigned truck
    if edited is not None:
        for row in edited.to_dict(orient="records"):
            update_priskirta(conn, c, row["id"], row["priskirtas_vilkikas"])
        st.success("✅ Assignments updated")
