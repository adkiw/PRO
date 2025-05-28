import streamlit as st

def priekaba_form():
    with st.form("priekaba_form", clear_on_submit=True):
        tipas = st.text_input("Priekabų tipas")
        numeris = st.text_input("Valstybinis numeris")
        marke = st.text_input("Markė")
        pagaminimo_metai = st.text_input("Pagaminimo metai")
        tech_apziura = st.date_input("Tech. apžiūra")
        submitted = st.form_submit_button("💾 Išsaugoti priekabą")
        if submitted:
            if not numeris:
                st.error("Numeris yra privalomas.")
                return None
            return {
                "priekabu_tipas": tipas.strip(),
                "numeris": numeris.strip(),
                "marke": marke.strip(),
                "pagaminimo_metai": pagaminimo_metai.strip(),
                "tech_apziura": str(tech_apziura)
            }
    return None
