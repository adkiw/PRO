import streamlit as st

from forms.nustatymai import nustatymai_form as nustatymai_form
from logic.nustatymai import get_all_categories, insert_lookup, delete_lookup

def show(conn, c):
    st.title("DISPO – Settings (lookup)")

    # 1. Enter or select category
    cats = get_all_categories(conn, c)
    col1, col2 = st.columns(2)
    selected = col1.selectbox("Existing category", ["" ] + cats)
    new_cat = col2.text_input("Or new category")
    kat = new_cat.strip() or selected

    if kat:
        st.subheader(f"Category: **{kat}**")
        # 2. Show existing values
        values = [v for v in c.execute(
            "SELECT reiksme FROM lookup WHERE kategorija=?", (kat,)
        ).fetchall()]
        st.write([v[0] for v in values] or "_(not found)_")

        # 3. Pridėti reikšmę
        rv = st.text_input("New value")
        if st.button("➕ Add"):
            insert_lookup(conn, c, kat, rv)
            st.experimental_rerun()

        # 4. Ištrinti reikšmę
        delv = st.selectbox("Delete", ["" ] + [v[0] for v in values])
        if st.button("🗑 Remove"):
            delete_lookup(conn, c, kat, delv)
            st.experimental_rerun()

    else:
        st.info("Select or enter a category above.")
