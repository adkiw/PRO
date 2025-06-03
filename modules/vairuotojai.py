diff --git a/forms/vairuotojai.py b/forms/vairuotojai.py
index 445d9d6a7d5b2aaf9f64af61bfb579dcd7f17c69..adfd0ad4c16e98c5deda5572cb634233acfb857e 100644
--- a/forms/vairuotojai.py
+++ b/forms/vairuotojai.py
@@ -1,26 +1,28 @@
 import streamlit as st
 
 def vairuotojas_form():
     """
-    Formos komponentas naujam vairuotojui.
-    Grąžina duomenis kaip žodyną arba None, jei nepateikta.
+    Form component for a new driver.
+    Returns a dict or None if not provided.
     """
     with st.form("vairuotojas_form", clear_on_submit=True):
-        vardas = st.text_input("Vardas")
-        pavarde = st.text_input("Pavardė")
-        gimimo_metai = st.text_input("Gimimo metai")
-        tautybe = st.text_input("Tautybė")
-        priskirtas_vilkikas = st.text_input("Priskirtas vilkikas")
-        submitted = st.form_submit_button("💾 Išsaugoti vairuotoją")
+        vardas = st.text_input("First name")
+        pavarde = st.text_input("Last name")
+        gimimo_metai = st.text_input("Birth year")
+        tautybe = st.text_input("Nationality")
+        priskirtas_vilkikas = st.text_input("Assigned truck")
+        submitted = st.form_submit_button("💾 Save driver")
         if submitted:
             if not vardas or not pavarde:
-                st.error("Vardas ir pavardė yra privalomi.")
+                st.error("First and last name are required.")
                 return None
             return {
                 "vardas": vardas.strip(),
                 "pavarde": pavarde.strip(),
                 "gimimo_metai": gimimo_metai.strip(),
                 "tautybe": tautybe.strip(),
                 "priskirtas_vilkikas": priskirtas_vilkikas.strip(),
             }
     return None
+
+render_form = vairuotojas_form
