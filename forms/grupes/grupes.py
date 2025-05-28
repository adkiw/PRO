import streamlit as st

def grupe_form():
    """
    Formos komponentas naujos grupės kūrimui.
    Grąžina duomenis kaip žodyną arba None, jei nepateikta.
    """
    with st.form("grupe_form", clear_on_submit=True):
        numeris = st.text_input("Grupės numeris")
        pavadinimas = st.text_input("Pavadinimas")
        aprasymas = st.text_area("Aprašymas")
        submitted = st.form_submit_button("💾 Išsaugoti grupę")
        if submitted:
            if not numeris or not pavadinimas:
                st.error("Numeris ir pavadinimas yra privalomi.")
                return None
            return {
                "numeris": numeris.strip(),
                "pavadinimas": pavadinimas.strip(),
                "aprasymas": aprasymas.strip()
            }
    return None
