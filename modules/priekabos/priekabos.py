import streamlit as st
from db import init_db
from logic.priekabos import (
    get_all_priekabos, insert_priekaba, update_priekaba
)
from forms.priekabos import priekaba_form
from tables.priekabos import show_priekabos_table

def show(conn=None):
    if conn is None:
        conn = init_db()
    st.title("DISPO – Priekabų valdymas")

    data = priekaba_form()
    if data:
        insert_priekaba(conn, data)
        st.success("✅ Priekaba įrašyta!")

    rows = get_all_priekabos(conn)
    edited = show_priekabos_table(rows)
    if not edited.empty:
        for rec in edited.to_dict(orient="records"):
            update_priekaba(conn, rec['id'], rec)
        st.success("✅ Priekabos atnaujintos!")
