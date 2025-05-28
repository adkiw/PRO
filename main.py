import streamlit as st
from db import init_db

# Importuoji modulius (privalo būti failai: modules/vilkikai.py ir t.t.)
from modules import (
    vilkikai,
    priekabos,
    kroviniai,
    darbuotojai,
    klientai,
    grupes,
    nustatymai
)

# Nustatom Streamlit puslapio konfigūraciją
st.set_page_config(layout="wide")
conn, c = init_db()

# Šoninis meniu
moduliai = [
    "DISPO", "Vilkikai", "Priekabos",
    "Kroviniai", "Darbuotojai", "Klientai",
    "Grupės", "Nustatymai"
]
modulis = st.sidebar.radio("📂 Pasirink modulį", moduliai)

# Pagrindinio turinio vaizdavimas
if modulis == "DISPO":
    st.title("DISPO sistema – pagrindinis langas")
    st.write("Pasirink modulį kairėje pusėje.")
elif modulis == "Vilkikai":
    vilkikai.show(conn, c)
elif modulis == "Priekabos":
    priekabos.show(conn, c)
elif modulis == "Kroviniai":
    kroviniai.show(conn, c)
elif modulis == "Darbuotojai":
    darbuotojai.show(conn, c)
elif modulis == "Klientai":
    klientai.show(conn, c)
elif modulis == "Grupės":
    grupes.show(conn, c)
elif modulis == "Nustatymai":
    nustatymai.show(conn, c)
