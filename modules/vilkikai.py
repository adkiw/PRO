diff --git a/forms/vilkikai.py b/forms/vilkikai.py
index 242c2fefbd2a152bf3647edbbbd2ca7961bcb871..69942397b84cb85e0570322bd456e5b187914e74 100644
--- a/forms/vilkikai.py
+++ b/forms/vilkikai.py
@@ -1,30 +1,32 @@
 import streamlit as st
 
 def vilkikas_form():
     """
-    Formos komponentas naujam vilkikui.
-    Grąžina dict arba None.
+    Form component for a new truck.
+    Returns a dict or None.
     """
     with st.form("vilkikas_form", clear_on_submit=True):
-        numeris = st.text_input("Numeris")
-        marke = st.text_input("Markė")
-        pagaminimo_metai = st.text_input("Pagaminimo metai")
-        tech_apziura = st.date_input("Tech. apžiūra")
-        vadybininkas = st.text_input("Vadybininkas")
-        vairuotojai = st.text_input("Vairuotojai (kableliais)")
-        priekaba = st.selectbox("Priekaba", [""] + get_priekabu_sarasas())
-        submitted = st.form_submit_button("💾 Išsaugoti vilkiką")
+        numeris = st.text_input("Number")
+        marke = st.text_input("Make")
+        pagaminimo_metai = st.text_input("Manufacture year")
+        tech_apziura = st.date_input("Inspection")
+        vadybininkas = st.text_input("Manager")
+        vairuotojai = st.text_input("Drivers (comma separated)")
+        priekaba = st.selectbox("Trailer", ["" ] + get_priekabu_sarasas())
+        submitted = st.form_submit_button("💾 Save truck")
         if submitted:
             if not numeris:
-                st.error("Numeris yra privalomas.")
+                st.error("Number is required.")
                 return None
             return {
                 "numeris": numeris.strip(),
                 "marke": marke.strip(),
                 "pagaminimo_metai": pagaminimo_metai.strip(),
                 "tech_apziura": str(tech_apziura),
                 "vadybininkas": vadybininkas.strip(),
                 "vairuotojai": vairuotojai.strip(),
                 "priekaba": priekaba.strip()
             }
     return None
+
+render_form = vilkikas_form
