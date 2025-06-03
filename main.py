diff --git a/main.py b/main.py
index 66df8892910fe7771611365b568de88be2b60c1b..6adccf6310f52148d6a42104ca32f23d0bb60b99 100644
--- a/main.py
+++ b/main.py
@@ -1,30 +1,30 @@
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
-conn = init_db()
+conn, c = init_db()
 
 PAGES = {
-    "Vilkikai":    show_vilkikai,
-    "Priekabos":    show_priekabos,
-    "Kroviniai":    show_kroviniai,
-    "Darbuotojai":  show_darbuotojai,
-    "Klientai":     show_klientai,
-    "Grupės":       show_grupes,
-    "Nustatymai":   show_nustatymai
+    "Trucks":       show_vilkikai,
+    "Trailers":     show_priekabos,
+    "Cargo":        show_kroviniai,
+    "Employees":    show_darbuotojai,
+    "Clients":      show_klientai,
+    "Groups":       show_grupes,
+    "Settings":     show_nustatymai
 }
 
-st.sidebar.title("DISPO moduliai")
-page = st.sidebar.radio("Pasirink modulį", list(PAGES.keys()))
+st.sidebar.title("DISPO modules")
+page = st.sidebar.radio("Select module", list(PAGES.keys()))
 
-# Kviečiame tik conn argumentą
-PAGES[page](conn)
+# Call selected page
+PAGES[page](conn, c)
