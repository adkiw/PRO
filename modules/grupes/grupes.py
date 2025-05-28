import streamlit as st
from db import init_db
from forms.grupes import grupe_form
from logic.grupes import get_grupes, insert_grupe, update_grupe
from tables.grupes import show_grupes_table

def show(conn=None):
    """
    DISPO – Grupės modulis.
    Leidžia kurti naujas grupes, peržiūrėti, redaguoti esamas.
    """
    if conn is None:
        conn = init_db()

    st.title("DISPO – Grupės")

    # 1) Sukurti naują grupę
    data = grupe_form()
    if data:
        insert_grupe(conn, data)
        st.success("✅ Grupė sukurta!")

    # 2) Pateikti lentelę ir gauti pakeitimus
    rows = get_grupes(conn)
    edited_df = show_grupes_table(rows)

    # 3) Atnaujinti pakeitimus DB
    if not edited_df.empty:
        for record in edited_df.to_dict(orient="records"):
            update_grupe(conn, record['id'], {
                "numeris": record["numeris"],
                "pavadinimas": record["pavadinimas"],
                "aprasymas": record["aprasymas"]
            })
        st.success("✅ Grupės duomenys atnaujinti!")
