import streamlit as st

def nustatymai_form(kategorijos):
    st.subheader("Add new value")
    kat = st.selectbox("Category", kategorijos)
    val = st.text_input("Value")
    if st.button("➕ Add"):
        if kat and val:
            return kat, val.strip()
    st.markdown("---")
    st.subheader("Delete value")
    kat2 = st.selectbox("Category (delete)", ["" ] + kategorijos, key="del_cat")
    val2 = st.selectbox("Value (delete)", ["" ] + (get_values_placeholder(kat2) if kat2 else []), key="del_val")
    if st.button("🗑️ Delete"):
        if kat2 and val2:
            return kat2, val2
    return None

render_form = nustatymai_form
