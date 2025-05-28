import streamlit as st
import pandas as pd

from forms.vilkikai import render_form as vilkikai_form
from logic.vilkikai import get_all_vilkikai, insert_vilkikas, update_priekaba
from tables.vilkikai import render_table as vilkikai_table

def show(conn, c):
    st.title("DISPO – Vilkikų valdymas")

    # 1. Įvedimo forma
    with st.expander("➕ Pridėti naują vilkiką", expanded=True):
        data = vilkikai_form(conn, c)
        if data and st.button("💾 Išsaugoti vilkiką"):
            insert_vilkikas(conn, c, data)
            st.success("✅ Vilkiką išsaugojau")

    # 2. Duomenų atvaizdavimas
    df = pd.DataFrame(
        get_all_vilkikai(conn, c),
        columns=["id", "numeris", "marke", "pagaminimo_metai",
                 "tech_apziura", "vadybininkas", "vairuotojai", "priekaba"]
    )
    edited = vilkikai_table(df, key="vilkikai")

    # 3. Atnaujinti priekabą, jei redagavo lenteleje
    if edited is not None:
        for row in edited.to_dict(orient="records"):
            update_priekaba(conn, c, row["id"], row["priekaba"])
        st.success("✅ Atnaujinau priekabas")
