import streamlit as st
from db import init_db
from logic.nustatymai import (
    get_categories, get_values, insert_value, delete_value
)
from forms.nustatymai import nustatymai_form

def show(conn=None):
    if conn is None:
        conn = init_db()
    st.title("DISPO – Nustatymai")

    cats = get_categories(conn)
    # rodyti esamas kategorijas su jų reikšmėmis
    for cat in cats:
        vals = get_values(conn, cat)
        st.write(f"**{cat}**:", ", ".join(vals) if vals else "_nerasta_")

    result = nustatymai_form(cats)
    if result:
        kat, val = result
        # decide insert or delete by context; pavyzdžiui, jei val jau egzistuoja – delete
        if val in get_values(conn, kat):
            delete_value(conn, kat, val)
            st.success(f"✅ Ištrinta: {val} iš {kat}")
        else:
            insert_value(conn, kat, val)
            st.success(f"✅ Pridėta: {val} į {kat}")
