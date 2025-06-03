import streamlit as st

def priekaba_form():
    with st.form("priekaba_form", clear_on_submit=True):
        tipas = st.text_input("Trailer type")
        numeris = st.text_input("License plate")
        marke = st.text_input("Make")
        pagaminimo_metai = st.text_input("Manufacture year")
        tech_apziura = st.date_input("Inspection")
        submitted = st.form_submit_button("💾 Save trailer")
        if submitted:
            if not numeris:
                st.error("Number is required.")
                return None
            return {
                "priekabu_tipas": tipas.strip(),
                "numeris": numeris.strip(),
                "marke": marke.strip(),
                "pagaminimo_metai": pagaminimo_metai.strip(),
                "tech_apziura": str(tech_apziura)
            }
    return None

render_form = priekaba_form
