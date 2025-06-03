import streamlit as st

def vilkikas_form():
    """
    Form component for a new truck.
    Returns a dict or None.
    """
    with st.form("vilkikas_form", clear_on_submit=True):
        numeris = st.text_input("Number")
        marke = st.text_input("Make")
        pagaminimo_metai = st.text_input("Manufacture year")
        tech_apziura = st.date_input("Inspection")
        vadybininkas = st.text_input("Manager")
        vairuotojai = st.text_input("Drivers (comma separated)")
        priekaba = st.selectbox("Trailer", ["" ] + get_priekabu_sarasas())
        submitted = st.form_submit_button("💾 Save truck")
        if submitted:
            if not numeris:
                st.error("Number is required.")
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

render_form = vilkikas_form
