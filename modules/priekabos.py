diff --git a/forms/priekabos.py b/forms/priekabos.py
index c2d0c4a694ab086df5fc3987bd7bf3b67db36039..be2a335ed2004476fc04e97b641f3c3b99718a25 100644
--- a/forms/priekabos.py
+++ b/forms/priekabos.py
@@ -1,22 +1,24 @@
 import streamlit as st
 
 def priekaba_form():
     with st.form("priekaba_form", clear_on_submit=True):
-        tipas = st.text_input("Priekabų tipas")
-        numeris = st.text_input("Valstybinis numeris")
-        marke = st.text_input("Markė")
-        pagaminimo_metai = st.text_input("Pagaminimo metai")
-        tech_apziura = st.date_input("Tech. apžiūra")
-        submitted = st.form_submit_button("💾 Išsaugoti priekabą")
+        tipas = st.text_input("Trailer type")
+        numeris = st.text_input("License plate")
+        marke = st.text_input("Make")
+        pagaminimo_metai = st.text_input("Manufacture year")
+        tech_apziura = st.date_input("Inspection")
+        submitted = st.form_submit_button("💾 Save trailer")
         if submitted:
             if not numeris:
-                st.error("Numeris yra privalomas.")
+                st.error("Number is required.")
                 return None
             return {
                 "priekabu_tipas": tipas.strip(),
                 "numeris": numeris.strip(),
                 "marke": marke.strip(),
                 "pagaminimo_metai": pagaminimo_metai.strip(),
                 "tech_apziura": str(tech_apziura)
             }
     return None
+
+render_form = priekaba_form
