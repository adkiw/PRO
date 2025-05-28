# forms/darbuotojai.py
import streamlit as st

def darbuotojai_form():
    st.subheader("💼 Naujas darbuotojas")

    vardas = st.text_input("Vardas")
    pavarde = st.text_input("Pavardė")
    pareigybe = st.text_input("Pareigybė")
    el_pastas = st.text_input("El. paštas")
    telefonas = st.text_input("Telefono numeris")
    grupe = st.text_input("Grupė")

    submitted = st.button("➕ Pridėti darbuotoją")
    if submitted:
        if not vardas or not pavarde:
            st.error("❌ Privalomi laukai: vardas ir pavardė")
        else:
            st.success(f"✅ Darbuotojas {vardas} {pavarde} pridėtas!")
            return {
                "vardas": vardas,
                "pavarde": pavarde,
                "pareigybe": pareigybe,
                "el_pastas": el_pastas,
                "telefonas": telefonas,
                "grupe": grupe
            }
    return None
# Čia bus forms darbuotojai moduliui
