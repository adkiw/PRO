import streamlit as st
import pandas as pd

from forms.klientai import render_form as klientai_form
from logic.klientai import get_all_klientai, insert_klientas, update_regionas
from tables.klientai import render_table as klientai_table

def show(conn, c):
    st.title("DISPO – Klientai")

    with st.expander("➕ Pridėti naują klientą", expanded=True):
        data = klientai_form(conn, c)
        if data and st.button("💾 Išsaugoti klientą"):
            insert_klientas(conn, c, data)
            st.success("✅ Klientą išsaugojau")

    df = pd.DataFrame(
        get_all_klientai(conn, c),
        columns=["id", "pavadinimas", "kontaktai", "salis",
                 "miestas", "regionas", "vat_numeris"]
    )
    edited = klientai_table(df, key="klientai")

    if edited is not None:
        for row in edited.to_dict(orient="records"):
            update_regionas(conn, c, row["id"], row["regionas"])
        st.success("✅ Atnaujinau regionus")
