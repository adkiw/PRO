import streamlit as st
from db import init_db
from logic.vilkikai import (
    get_vilkikai, insert, update_priekaba, get_all_priekabos
)
from forms.vilkikai import vilkikas_form
from tables.vilkikai import show_vilkikai_table

def show(conn=None):
    if conn is None:
        conn = init_db()
    st.title("DISPO – Vilkikų valdymas")

    # 1) Įvedimo forma
    data = vilkikas_form()
    if data:
        insert(conn, data)
        st.success("✅ Vilkikas įrašytas!")

    # 2) Lentelė ir redagavimas
    rows = get_vilkikai(conn)
    edited = show_vilkikai_table(rows)
    if not edited.empty:
        for rec in edited.to_dict(orient="records"):
            update_priekaba(conn, rec['id'], rec['priekaba'])
        st.success("✅ Priekabos atnaujintos!")
