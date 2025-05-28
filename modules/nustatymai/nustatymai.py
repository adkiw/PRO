import streamlit as st

from forms.nustatymai import render_form as nustatymai_form
from logic.nustatymai import get_all_categories, insert_lookup, delete_lookup

def show(conn, c):
    st.title("DISPO – Nustatymai (lookup)")

    # 1. Įvesti / pasirinkti kategoriją
    cats = get_all_categories(conn, c)
    col1, col2 = st.columns(2)
    selected = col1.selectbox("Esama kategorija", [""] + cats)
    new_cat = col2.text_input("Arba nauja kategorija")
    kat = new_cat.strip() or selected

    if kat:
        st.subheader(f"Kategorija: **{kat}**")
        # 2. Rodyti esamas reikšmes
        values = [v for v in c.execute(
            "SELECT reiksme FROM lookup WHERE kategorija=?", (kat,)
        ).fetchall()]
        st.write([v[0] for v in values] or "_(nerasta)_")

        # 3. Pridėti reikšmę
        rv = st.text_input("Nauja reikšmė")
        if st.button("➕ Pridėti"):
            insert_lookup(conn, c, kat, rv)
            st.experimental_rerun()

        # 4. Ištrinti reikšmę
        delv = st.selectbox("Ištrinti", [""] + [v[0] for v in values])
        if st.button("🗑 Pašalinti"):
            delete_lookup(conn, c, kat, delv)
            st.experimental_rerun()

    else:
        st.info("Pasirink arba įvesk kategoriją aukščiau.")
