# modules/vilkikai.py

import streamlit as st
import pandas as pd

from forms.vilkikai import render_form  # tavo įvedimo forma
from logic.vilkikai import get_all_vilkikai, insert_vilkikas, update_priekaba
from tables.vilkikai import render_table   # tavo lentelės atvaizdavimas

def show(conn):
    st.title("DISPO – Vilkikų valdymas")

    # 1) Rodyti įvedimo formą ir gauti duomenis
    with st.expander("➕ Pridėti naują vilkiką", expanded=True):
        data = render_form(conn)
        if data and st.button("💾 Išsaugoti vilkiką"):
            insert_vilkikas(conn, data)
            st.success("✅ Vilkiką išsaugojau")

    # 2) Nuskaityti visus vilkikus
    df = pd.DataFrame(get_all_vilkikai(conn),
                      columns=[
                          "id", "numeris", "marke", "pagaminimo_metai",
                          "tech_apziura", "vadybininkas", "vairuotojai", "priekaba"
                      ])

    # 3) Atvaizduoti lentelę su galimybe redaguoti priekabą
    edited = render_table(df, key="vilkikai_table")

    # 4) Jei kažką pakeitėm, atnaujinti DB
    if edited is not None and not edited.empty:
        for row in edited.to_dict(orient="records"):
            update_priekaba(conn, row["id"], row["priekaba"])
        st.success("✅ Atnaujinau priekabas")
