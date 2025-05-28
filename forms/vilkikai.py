import streamlit as st

def vilkikas_form():
    """
    Formos komponentas naujam vilkikui.
    Grąžina dict arba None.
    """
    with st.form("vilkikas_form", clear_on_submit=True):
        numeris = st.text_input("Numeris")
        marke = st.text_input("Markė")
        pagaminimo_metai = st.text_input("Pagaminimo metai")
        tech_apziura = st.date_input("Tech. apžiūra")
        vadybininkas = st.text_input("Vadybininkas")
        vairuotojai = st.text_input("Vairuotojai (kableliais)")
        priekaba = st.selectbox("Priekaba", [""] + get_priekabu_sarasas())
        submitted = st.form_submit_button("💾 Išsaugoti vilkiką")
        if submitted:
            if not numeris:
                st.error("Numeris yra privalomas.")
                return None
            return {
                "numeris": numeris.strip(),
                "marke": marke.strip(),
                "pagaminimo_metai": pagaminimo_metai.strip(),
                "tech_apziura": str(tech_apziura),
                "vadybininkas": vadybininkas.strip(),
                "vairuotojai": vairuotojai.strip(),
                "priekaba": priekaba.strip()
            }
    return None
