import streamlit as st
import pandas as pd

from forms.grupes import grupe_form as grupes_form
from logic.grupes import get_all_grupes, insert_grupe, update_aprasymas
from table.grupes import show_grupes_table as grupes_table

def show(conn, c):
    st.title("DISPO – Groups")

    with st.expander("➕ Add new group", expanded=True):
        data = grupes_form(conn, c)
        if data and st.button("💾 Save group"):
            insert_grupe(conn, c, data)
            st.success("✅ Group saved")

    df = pd.DataFrame(
        get_all_grupes(conn, c),
        columns=["id", "numeris", "pavadinimas", "aprasymas"]
    )
    edited = grupes_table(df, key="grupes")

    if edited is not None:
        for row in edited.to_dict(orient="records"):
            update_aprasymas(conn, c, row["id"], row["aprasymas"])
        st.success("✅ Descriptions updated")
