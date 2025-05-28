import streamlit as st
import pandas as pd

from forms.grupes import render_form as grupes_form
from logic.grupes import get_all_grupes, insert_grupe, update_aprasymas
from tables.grupes import render_table as grupes_table

def show(conn, c):
    st.title("DISPO – Grupės")

    with st.expander("➕ Pridėti naują grupę", expanded=True):
        data = grupes_form(conn, c)
        if data and st.button("💾 Išsaugoti grupę"):
            insert_grupe(conn, c, data)
            st.success("✅ Grupę išsaugojau")

    df = pd.DataFrame(
        get_all_grupes(conn, c),
        columns=["id", "numeris", "pavadinimas", "aprasymas"]
    )
    edited = grupes_table(df, key="grupes")

    if edited is not None:
        for row in edited.to_dict(orient="records"):
            update_aprasymas(conn, c, row["id"], row["aprasymas"])
        st.success("✅ Atnaujinau aprašymus")
