import streamlit as st
import pandas as pd

from forms.vilkikai import vilkikas_form as vilkikai_form
from logic.vilkikai import get_all_vilkikai, insert_vilkikas, update_priekaba
from table.vilkikai import show_vilkikai_table as vilkikai_table

def show(conn, c):
    st.title("DISPO – Truck Management")

    # 1. Input form
    with st.expander("➕ Add new truck", expanded=True):
        data = vilkikai_form(conn, c)
        if data and st.button("💾 Save truck"):
            insert_vilkikas(conn, c, data)
            st.success("✅ Truck saved")

    # 2. Display data
    df = pd.DataFrame(
        get_all_vilkikai(conn, c),
        columns=["id", "numeris", "marke", "pagaminimo_metai",
                 "tech_apziura", "vadybininkas", "vairuotojai", "priekaba"]
    )
    edited = vilkikai_table(df, key="vilkikai")

    # 3. Update trailer if edited in table
    if edited is not None:
        for row in edited.to_dict(orient="records"):
            update_priekaba(conn, c, row["id"], row["priekaba"])
        st.success("✅ Updated trailers")
