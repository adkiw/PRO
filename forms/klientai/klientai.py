# forms/klientai.py
import streamlit as st
from typing import Dict, Any

def klientai_form() -> Dict[str, Any] | None:
    st.subheader("📋 Klientų valdymas")
    with st.form("klientai_form", clear_on_submit=False):
        pavadinimas = st.text_input("Įmonės pavadinimas")
        kontaktai = st.text_input("Kontaktai")
        salis = st.text_input("Šalis")
        miestas = st.text_input("Miestas")
        regionas = st.text_input("Regionas")
        vat_numeris = st.text_input("PVM numeris")

        submitted = st.form_submit_button("💾 Išsaugoti klientą")
        if submitted:
            if not pavadinimas:
                st.error("❌ Įmonės pavadinimas būtinas.")
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
