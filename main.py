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
conn, c = init_db()

PAGES = {
    "Trucks":       show_vilkikai,
    "Trailers":     show_priekabos,
    "Cargo":        show_kroviniai,
    "Employees":    show_darbuotojai,
    "Clients":      show_klientai,
    "Groups":       show_grupes,
    "Settings":     show_nustatymai
}

st.sidebar.title("DISPO modules")
page = st.sidebar.radio("Select module", list(PAGES.keys()))

# Call selected page
PAGES[page](conn, c)
