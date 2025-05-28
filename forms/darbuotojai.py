import streamlit as st

def darbuotojas_form():
    """
    Formos komponentas naujam darbuotojui.
    Grąžina duomenis kaip žodyną arba None, jei nepateikta.
    """
    with st.form("darbuotojas_form", clear_on_submit=True):
        vardas = st.text_input("Vardas")
        pavarde = st.text_input("Pavardė")
        pareigybe = st.text_input("Pareigybė")
        el_pastas = st.text_input("El. paštas")
        telefonas = st.text_input("Telefonas")
        grupe = st.text_input("Grupė")
        submitted = st.form_submit_button("💾 Išsaugoti darbuotoją")
        if submitted:
            if not vardas or not pavarde:
                st.error("Vardas ir pavardė yra privalomi.")
                return None
            return {
                "vardas": vardas.strip(),
                "pavarde": pavarde.strip(),
                "pareigybe": pareigybe.strip(),
                "el_pastas": el_pastas.strip(),
                "telefonas": telefonas.strip(),
                "grupe": grupe.strip(),
            }
    return None
