import streamlit as st
import pandas as pd

from forms.kroviniai import krovinio_form as kroviniai_form
from logic.kroviniai import get_all_kroviniai, insert_krovinys, update_busena
from table.kroviniai import show_kroviniai_table as kroviniai_table

def show(conn, c):
    st.title("DISPO – Cargo Management")

    with st.expander("➕ Add new cargo", expanded=True):
        data = kroviniai_form(conn, c)
        if data and st.button("💾 Save cargo"):
            insert_krovinys(conn, c, data)
            st.success("✅ Cargo saved")

    df = pd.DataFrame(
        get_all_kroviniai(conn, c),
        columns=[
            "id", "klientas", "uzsakymo_numeris", "pakrovimo_data",
            "pakrovimo_laikas_nuo", "pakrovimo_laikas_iki",
            "iskrovimo_data", "iskrovimo_laikas_nuo", "iskrovimo_laikas_iki",
            "pakrovimo_salis", "pakrovimo_miestas", "iskrovimo_salis",
            "iskrovimo_miestas", "vilkikas", "priekaba",
            "atsakingas_vadybininkas", "kilometrai","frachtas",
            "svoris", "paleciu_skaicius", "busena"
        ]
    )
    edited = kroviniai_table(df, key="kroviniai")

    if edited is not None:
        for row in edited.to_dict(orient="records"):
            update_busena(conn, c, row["id"], row["busena"])
        st.success("✅ Statuses updated")
