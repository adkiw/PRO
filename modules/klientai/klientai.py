import streamlit as st
from db import init_db
from forms.klientai import klientas_form
from logic.klientai import get_all_klientai, insert_klientas, update_klientas
from tables.klientai import show_klientai_table

def show(conn=None):
    """
    DISPO – Klientų modulis.
    Rodo įvedimo formą, lentelę su redagavimu ir įrašymo/atnaujinimo galimybe.
    """
    if conn is None:
        conn = init_db()

    st.title("DISPO – Klientų valdymas")

    # 1) Formos duomenys naujam klientui
    data = klientas_form()
    if data:
        insert_klientas(conn, data)
        st.success("✅ Klientas įrašytas!")

    # 2) Rodome klientų lentelę
    rows = get_all_klientai(conn)
    edited_df = show_klientai_table(rows)

    # 3) Atnaujiname pakeitimus lentelėje
    if not edited_df.empty:
        for record in edited_df.to_dict(orient="records"):
            update_klientas(conn, record['id'], record)
        st.success("✅ Klientų duomenys atnaujinti!")
