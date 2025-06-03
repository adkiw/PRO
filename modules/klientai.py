diff --git a/forms/klientai.py b/forms/klientai.py
index 198589f70273696d993391ad598eb89d1f95f6b1..0073d981802478a3dfa14bac4780a18c0be95447 100644
--- a/forms/klientai.py
+++ b/forms/klientai.py
@@ -1,28 +1,30 @@
 # forms/klientai.py
 import streamlit as st
 from typing import Dict, Any
 
 def klientai_form() -> Dict[str, Any] | None:
-    st.subheader("📋 Klientų valdymas")
+    st.subheader("📋 Client management")
     with st.form("klientai_form", clear_on_submit=False):
-        pavadinimas = st.text_input("Įmonės pavadinimas")
-        kontaktai = st.text_input("Kontaktai")
-        salis = st.text_input("Šalis")
-        miestas = st.text_input("Miestas")
-        regionas = st.text_input("Regionas")
-        vat_numeris = st.text_input("PVM numeris")
+        pavadinimas = st.text_input("Company name")
+        kontaktai = st.text_input("Contacts")
+        salis = st.text_input("Country")
+        miestas = st.text_input("City")
+        regionas = st.text_input("Region")
+        vat_numeris = st.text_input("VAT number")
 
-        submitted = st.form_submit_button("💾 Išsaugoti klientą")
+        submitted = st.form_submit_button("💾 Save client")
         if submitted:
             if not pavadinimas:
-                st.error("❌ Įmonės pavadinimas būtinas.")
+                st.error("❌ Company name is required.")
                 return None
             return {
                 "pavadinimas": pavadinimas,
                 "kontaktai": kontaktai,
                 "salis": salis,
                 "miestas": miestas,
                 "regionas": regionas,
                 "vat_numeris": vat_numeris
             }
     return None
+
+render_form = klientai_form
