import streamlit as st
from db import init_db
from forms.vairuotojai import vairuotojas_form
from logic.vairuotojai import (
    get_all_vairuotojai,
    insert_vairuotojas,
    update_vairuotojas,
    delete_vairuotojas
)
from tables.vairuotojai import show_vairuotojai_table

def show(conn=None):
    """
    DISPO – Vairuotojų modulis.
    Leidžia kurti, peržiūrėti, redaguoti ir trinti vairuotojus.
    """
    if conn is None:
        conn = init_db()

    st.title("DISPO – Vairuotojų valdymas")

    # 1) Formos duomenys
    data = vairuotojas_form()
    if data:
        insert_vairuotojas(conn, data)
        st.success("✅ Vairuotojas įrašytas!")

    # 2) Rodome lentelę ir gauname redaguotus įrašus
    rows = get_all_vairuotojai(conn)
    edited_df = show_vairuotojai_table(rows)

    # 3) Atnaujiname pakeitimus DB
    if not edited_df.empty:
        for rec in edited_df.to_dict(orient="records"):
            update_vairuotojas(conn, rec['id'], rec)
        st.success("✅ Vairuotojų duomenys atnaujinti!")

    # 4) Ištrynimas
    st.markdown("---")
    id_to_delete = st.number_input("ID ištrynimui:", min_value=1, step=1)
    if st.button("🗑️ Ištrinti vairuotoją"):
        delete_vairuotojas(conn, int(id_to_delete))
        st.success(f"✅ Vairuotojas su ID {id_to_delete} ištrintas.")
