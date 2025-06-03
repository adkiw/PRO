diff --git a/forms/nustatymai.py b/forms/nustatymai.py
index 56bd5f2abc457db14e1bc4b27b288bb82a9830f9..89be073513b83277d506fa7577a16649c5e2a613 100644
--- a/forms/nustatymai.py
+++ b/forms/nustatymai.py
@@ -1,17 +1,19 @@
 import streamlit as st
 
 def nustatymai_form(kategorijos):
-    st.subheader("Pridėti naują reikšmę")
-    kat = st.selectbox("Kategorija", kategorijos)
-    val = st.text_input("Reikšmė")
-    if st.button("➕ Pridėti"):
+    st.subheader("Add new value")
+    kat = st.selectbox("Category", kategorijos)
+    val = st.text_input("Value")
+    if st.button("➕ Add"):
         if kat and val:
             return kat, val.strip()
     st.markdown("---")
-    st.subheader("Ištrinti reikšmę")
-    kat2 = st.selectbox("Kategorija (ištrinti)", [""] + kategorijos, key="del_cat")
-    val2 = st.selectbox("Reikšmė (ištrinti)", [""] + (get_values_placeholder(kat2) if kat2 else []), key="del_val")
-    if st.button("🗑️ Ištrinti"):
+    st.subheader("Delete value")
+    kat2 = st.selectbox("Category (delete)", ["" ] + kategorijos, key="del_cat")
+    val2 = st.selectbox("Value (delete)", ["" ] + (get_values_placeholder(kat2) if kat2 else []), key="del_val")
+    if st.button("🗑️ Delete"):
         if kat2 and val2:
             return kat2, val2
     return None
+
+render_form = nustatymai_form
