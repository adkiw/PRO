import streamlit as st
import pandas as pd

from forms.priekabos import render_form as priekabos_form
from logic.priekabos import get_all_priekabos, insert_priekaba, update_priskirta
from tables.priekabos import render_table as priekabos_table

def show(conn, c):
    st.title("DISPO – Priekabų valdymas")

    # 1. Įvedimo forma
    with st.expander("➕ Pridėti naują priekabą", expanded=True):
        data = priekabos_form(conn, c)
        if data and st.button("💾 Išsaugoti priekabą"):
            insert_priekaba(conn, c, data)
            st.success("✅ Priekabą išsaugojau")

    # 2. Lentelė
    df = pd.DataFrame(
        get_all_priekabos(conn, c),
        columns=["id", "tipas", "numeris", "marke",
                 "pagaminimo_metai", "tech_apziura", "priskirtas_vilkikas"]
    )
    edited = priekabos_table(df, key="priekabos")

    # 3. Atnaujinti priskirtą vilkiką
    if edited is not None:
        for row in edited.to_dict(orient="records"):
            update_priskirta(conn, c, row["id"], row["priskirtas_vilkikas"])
        st.success("✅ Atnaujinau priskyrimus")
