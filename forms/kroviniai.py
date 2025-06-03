# forms/kroviniai.py
import streamlit as st

from datetime import date, time
from typing import Dict, Any


def krovinio_form() -> Dict[str, Any] | None:
    st.subheader("📋 Cargo management")
    with st.form("krovinys_form", clear_on_submit=False):
        klientas = st.text_input("Client")
        uzsakymo_numeris = st.text_input("Order number")
        pakrovimo_numeris = st.text_input("Loading number")
        col1, col2 = st.columns(2)
        pakrovimo_data = col1.date_input("Loading date", date.today())
        pakrovimo_laikas_nuo = col1.time_input("Time from (loading)", time(8, 0))
        pakrovimo_laikas_iki = col1.time_input("Time to (loading)", time(17, 0))
        iskrovimo_data = col2.date_input("Unloading date", pakrovimo_data)
        iskrovimo_laikas_nuo = col2.time_input("Time from (unloading)", time(8, 0))
        iskrovimo_laikas_iki = col2.time_input("Time to (unloading)", time(17, 0))

        pakrovimo_salis = st.text_input("Loading country")
        pakrovimo_miestas = st.text_input("Loading city")
        iskrovimo_salis = st.text_input("Unloading country")
        iskrovimo_miestas = st.text_input("Unloading city")

        vilkikas = st.text_input("Truck")
        priekaba = st.text_input("Trailer")
        atsakingas_vadybininkas = st.text_input("Responsible manager")

        kilometrai = st.number_input("Kilometers", min_value=0, value=0)
        frachtas = st.number_input("Freight (€)", min_value=0.0, value=0.0)
        svoris = st.number_input("Weight (kg)", min_value=0, value=0)
        paleciu_skaicius = st.number_input("Number of pallets", min_value=0, value=0)

        busena = st.selectbox(
            "Status", ["planned", "loaded", "unloaded"]
        )

        submitted = st.form_submit_button("💾 Save cargo")
        if submitted:
            # Validacija
            if not klientas or not uzsakymo_numeris:
                st.error("❌ Required fields: Client and Order number.")
                return None
            if pakrovimo_data > iskrovimo_data:
                st.error("❌ Loading date cannot be later than unloading date.")
                return None

            return {
                "klientas": klientas,
                "uzsakymo_numeris": uzsakymo_numeris,
                "pakrovimo_numeris": pakrovimo_numeris,
                "pakrovimo_data": str(pakrovimo_data),
                "pakrovimo_laikas_nuo": str(pakrovimo_laikas_nuo),
                "pakrovimo_laikas_iki": str(pakrovimo_laikas_iki),
                "iskrovimo_data": str(iskrovimo_data),
                "iskrovimo_laikas_nuo": str(iskrovimo_laikas_nuo),
                "iskrovimo_laikas_iki": str(iskrovimo_laikas_iki),
                "pakrovimo_salis": pakrovimo_salis,
                "pakrovimo_miestas": pakrovimo_miestas,
                "iskrovimo_salis": iskrovimo_salis,
                "iskrovimo_miestas": iskrovimo_miestas,
                "vilkikas": vilkikas,
                "priekaba": priekaba,
                "atsakingas_vadybininkas": atsakingas_vadybininkas,
                "kilometrai": kilometrai,
                "frachtas": frachtas,
                "svoris": svoris,
                "paleciu_skaicius": paleciu_skaicius,
                "busena": busena
            }
    return None

render_form = krovinio_form
