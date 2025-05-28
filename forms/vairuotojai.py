import streamlit as st

def vairuotojas_form():
    """
    Formos komponentas naujam vairuotojui.
    Grąžina duomenis kaip žodyną arba None, jei nepateikta.
    """
    with st.form("vairuotojas_form", clear_on_submit=True):
        vardas = st.text_input("Vardas")
        pavarde = st.text_input("Pavardė")
        gimimo_metai = st.text_input("Gimimo metai")
        tautybe = st.text_input("Tautybė")
        priskirtas_vilkikas = st.text_input("Priskirtas vilkikas")
        submitted = st.form_submit_button("💾 Išsaugoti vairuotoją")
        if submitted:
            if not vardas or not pavarde:
                st.error("Vardas ir pavardė yra privalomi.")
                return None
            return {
                "vardas": vardas.strip(),
                "pavarde": pavarde.strip(),
                "gimimo_metai": gimimo_metai.strip(),
                "tautybe": tautybe.strip(),
                "priskirtas_vilkikas": priskirtas_vilkikas.strip(),
            }
    return None
