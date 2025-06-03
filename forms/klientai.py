# forms/klientai.py
import streamlit as st
from typing import Dict, Any

def klientai_form() -> Dict[str, Any] | None:
    st.subheader("📋 Client management")
    with st.form("klientai_form", clear_on_submit=False):
        pavadinimas = st.text_input("Company name")
        kontaktai = st.text_input("Contacts")
        salis = st.text_input("Country")
        miestas = st.text_input("City")
        regionas = st.text_input("Region")
        vat_numeris = st.text_input("VAT number")

        submitted = st.form_submit_button("💾 Save client")
        if submitted:
            if not pavadinimas:
                st.error("❌ Company name is required.")
                return None
            return {
                "pavadinimas": pavadinimas,
                "kontaktai": kontaktai,
                "salis": salis,
                "miestas": miestas,
                "regionas": regionas,
                "vat_numeris": vat_numeris
            }
    return None

render_form = klientai_form
