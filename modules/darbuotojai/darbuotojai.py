# modules/darbuotojai.py

import streamlit as st
from db import init_db
from forms.darbuotojai import darbuotojas_form
from logic.darbuotojai import (
    get_all_darbuotojai,
    insert_darbuotojas,
    update_darbuotojas,
    delete_darbuotojas
)
from tables.darbuotojai import show_darbuotojai_table

def show(conn=None):
    """
    DISPO – Darbuotojų modulis.
    Leidžia kurti, peržiūrėti, redaguoti ir trinti darbuotojus.
    """
    if conn is None:
        conn = init_db()

    st.title("DISPO – Darbuotojų valdymas")

    # 1) Naujo darbuotojo forma
    data = darbuotojas_form()
    if data:
        insert_darbuotojas(conn, data)
        st.success("✅ Darbuotojas įrašytas!")

    # 2) Lentelė ir redagavimo editorius
    rows = get_all_darbuotojai(conn)
    edited_df = show_darbuotojai_table(rows)

    # 3) Atnaujiname pakeitimus
    if not edited_df.empty:
        for rec in edited_df.to_dict(orient="records"):
            update_darbuotojas(conn, rec["id"], rec)
        st.success("✅ Darbuotojų duomenys atnaujinti!")

    # 4) Trinimas
    st.markdown("---")
    id_to_delete = st.number_input("ID ištrynimui:", min_value=1, step=1)
    if st.button("🗑️ Ištrinti darbuotoją"):
        delete_darbuotojas(conn, int(id_to_delete))
        st.success(f"✅ Darbuotojas su ID {id_to_delete} ištrintas.")
