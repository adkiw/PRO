# modules/kroviniai.py
import streamlit as st
from db import init_db
from forms.kroviniai import krovinio_form
from logic.kroviniai import (
    get_all_kroviniai, insert_krovinys,
    update_krovinys, delete_krovinys
)
from tables.kroviniai import show_kroviniai_table

def show(conn=None):
    """
    DISPO – Krovinių modulis.
    Rodoma forma, lentelė su redagavimu ir trynimu.
    """
    if conn is None:
        conn = init_db()

    st.title("DISPO – Krovinių valdymas")

    # 1) Formos duomenys
    data = krovinio_form()
    if data:
        insert_krovinys(conn, data)
        st.success("✅ Krovinys įrašytas!")

    # 2) Rodome lentelę ir gauname redaguotus įrašus
    rows = get_all_kroviniai(conn)
    edited_df = show_kroviniai_table(rows)

    # 3) Jei yra pakeitimų – atnaujiname DB
    if not edited_df.empty:
        for record in edited_df.to_dict(orient="records"):
            update_krovinys(conn, record['id'], record)
        st.success("✅ Lentelė atnaujinta!")

    # 4) Istorinis ištrynimas
    st.markdown("---")
    id_to_delete = st.number_input("ID ištrynimui:", min_value=1, step=1)
    if st.button("🗑️ Ištrinti krovinį"):
        delete_krovinys(conn, int(id_to_delete))
        st.success(f"✅ Krovinys su ID {id_to_delete} ištrintas.")
