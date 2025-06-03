import streamlit as st
import pandas as pd

from forms.klientai import klientai_form as klientai_form
from logic.klientai import get_all_klientai, insert_klientas, update_regionas
from table.klientai import show_klientai_table as klientai_table

def show(conn, c):
    st.title("DISPO – Clients")

    with st.expander("➕ Add new client", expanded=True):
        data = klientai_form(conn, c)
        if data and st.button("💾 Save client"):
            insert_klientas(conn, c, data)
            st.success("✅ Client saved")

    df = pd.DataFrame(
        get_all_klientai(conn, c),
        columns=["id", "pavadinimas", "kontaktai", "salis",
                 "miestas", "regionas", "vat_numeris"]
    )
    edited = klientai_table(df, key="klientai")

    if edited is not None:
        for row in edited.to_dict(orient="records"):
            update_regionas(conn, c, row["id"], row["regionas"])
        st.success("✅ Regions updated")
