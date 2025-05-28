import streamlit as st
from db import init_db

# importuojame tik show funkcijas
from modules.vilkikai     import show as show_vilkikai
from modules.priekabos     import show as show_priekabos
from modules.kroviniai     import show as show_kroviniai
from modules.darbuotojai   import show as show_darbuotojai
from modules.klientai      import show as show_klientai
from modules.grupes        import show as show_grupes
from modules.nustatymai    import show as show_nustatymai

st.set_page_config(layout="wide")
conn = init_db()

PAGES = {
    "Vilkikai":    show_vilkikai,
    "Priekabos":    show_priekabos,
    "Kroviniai":    show_kroviniai,
    "Darbuotojai":  show_darbuotojai,
    "Klientai":     show_klientai,
    "Grupės":       show_grupes,
    "Nustatymai":   show_nustatymai
}

st.sidebar.title("DISPO moduliai")
page = st.sidebar.radio("Pasirink modulį", list(PAGES.keys()))

# Kviečiame tik conn argumentą
PAGES[page](conn)
