diff --git a/forms/darbuotojai.py b/forms/darbuotojai.py
index cd8e474cbd2a828b1d3031ba280f4eac6a3dccdb..aec926dcdda03804affa5390b00c8af2374aa881 100644
--- a/forms/darbuotojai.py
+++ b/forms/darbuotojai.py
@@ -1,28 +1,30 @@
 import streamlit as st
 
 def darbuotojas_form():
     """
-    Formos komponentas naujam darbuotojui.
-    Grąžina duomenis kaip žodyną arba None, jei nepateikta.
+    Form component for a new employee.
+    Returns data as a dict or None if not provided.
     """
     with st.form("darbuotojas_form", clear_on_submit=True):
-        vardas = st.text_input("Vardas")
-        pavarde = st.text_input("Pavardė")
-        pareigybe = st.text_input("Pareigybė")
-        el_pastas = st.text_input("El. paštas")
-        telefonas = st.text_input("Telefonas")
-        grupe = st.text_input("Grupė")
-        submitted = st.form_submit_button("💾 Išsaugoti darbuotoją")
+        vardas = st.text_input("First name")
+        pavarde = st.text_input("Last name")
+        pareigybe = st.text_input("Position")
+        el_pastas = st.text_input("Email")
+        telefonas = st.text_input("Phone")
+        grupe = st.text_input("Group")
+        submitted = st.form_submit_button("💾 Save employee")
         if submitted:
             if not vardas or not pavarde:
-                st.error("Vardas ir pavardė yra privalomi.")
+                st.error("First and last name are required.")
                 return None
             return {
                 "vardas": vardas.strip(),
                 "pavarde": pavarde.strip(),
                 "pareigybe": pareigybe.strip(),
                 "el_pastas": el_pastas.strip(),
                 "telefonas": telefonas.strip(),
                 "grupe": grupe.strip(),
             }
     return None
+
+render_form = darbuotojas_form
