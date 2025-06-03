import streamlit as st

def darbuotojas_form():
    """
    Form component for a new employee.
    Returns data as a dict or None if not provided.
    """
    with st.form("darbuotojas_form", clear_on_submit=True):
        vardas = st.text_input("First name")
        pavarde = st.text_input("Last name")
        pareigybe = st.text_input("Position")
        el_pastas = st.text_input("Email")
        telefonas = st.text_input("Phone")
        grupe = st.text_input("Group")
        submitted = st.form_submit_button("💾 Save employee")
        if submitted:
            if not vardas or not pavarde:
                st.error("First and last name are required.")
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

render_form = darbuotojas_form
