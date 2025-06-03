import streamlit as st

def grupe_form():
    """
    Form component for creating a new group.
    Returns a dict or None if not provided.
    """
    with st.form("grupe_form", clear_on_submit=True):
        numeris = st.text_input("Group number")
        pavadinimas = st.text_input("Name")
        aprasymas = st.text_area("Description")
        submitted = st.form_submit_button("💾 Save group")
        if submitted:
            if not numeris or not pavadinimas:
                st.error("Number and name are required.")
                return None
            return {
                "numeris": numeris.strip(),
                "pavadinimas": pavadinimas.strip(),
                "aprasymas": aprasymas.strip()
            }
    return None

render_form = grupe_form
