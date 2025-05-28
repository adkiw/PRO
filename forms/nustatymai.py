import streamlit as st

def nustatymai_form(kategorijos):
    st.subheader("Pridėti naują reikšmę")
    kat = st.selectbox("Kategorija", kategorijos)
    val = st.text_input("Reikšmė")
    if st.button("➕ Pridėti"):
        if kat and val:
            return kat, val.strip()
    st.markdown("---")
    st.subheader("Ištrinti reikšmę")
    kat2 = st.selectbox("Kategorija (ištrinti)", [""] + kategorijos, key="del_cat")
    val2 = st.selectbox("Reikšmė (ištrinti)", [""] + (get_values_placeholder(kat2) if kat2 else []), key="del_val")
    if st.button("🗑️ Ištrinti"):
        if kat2 and val2:
            return kat2, val2
    return None
