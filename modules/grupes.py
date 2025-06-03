diff --git a/forms/grupes.py b/forms/grupes.py
index 945874455405b8476356894a8a6e40ecdd3b1748..b8a421cb7475088a5ae8f3864a6418dfe5feca1d 100644
--- a/forms/grupes.py
+++ b/forms/grupes.py
@@ -1,22 +1,24 @@
 import streamlit as st
 
 def grupe_form():
     """
-    Formos komponentas naujos grupės kūrimui.
-    Grąžina duomenis kaip žodyną arba None, jei nepateikta.
+    Form component for creating a new group.
+    Returns a dict or None if not provided.
     """
     with st.form("grupe_form", clear_on_submit=True):
-        numeris = st.text_input("Grupės numeris")
-        pavadinimas = st.text_input("Pavadinimas")
-        aprasymas = st.text_area("Aprašymas")
-        submitted = st.form_submit_button("💾 Išsaugoti grupę")
+        numeris = st.text_input("Group number")
+        pavadinimas = st.text_input("Name")
+        aprasymas = st.text_area("Description")
+        submitted = st.form_submit_button("💾 Save group")
         if submitted:
             if not numeris or not pavadinimas:
-                st.error("Numeris ir pavadinimas yra privalomi.")
+                st.error("Number and name are required.")
                 return None
             return {
                 "numeris": numeris.strip(),
                 "pavadinimas": pavadinimas.strip(),
                 "aprasymas": aprasymas.strip()
             }
     return None
+
+render_form = grupe_form
