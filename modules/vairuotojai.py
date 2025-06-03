import streamlit as st
import pandas as pd

from forms.vairuotojai import vairuotojas_form as vairuotojai_form
from logic.vairuotojai import get_all_vairuotojai, insert_vairuotojas, update_vilkikas
from table.vairuotojai import show_vairuotojai_table as vairuotojai_table

def show(conn, c):
    st.title("DISPO – Drivers")

    with st.expander("➕ Add new driver", expanded=True):
        data = vairuotojai_form(conn, c)
        if data and st.button("💾 Save driver"):
            insert_vairuotojas(conn, c, data)
            st.success("✅ Driver saved")

    df = pd.DataFrame(
        get_all_vairuotojai(conn, c),
        columns=["id", "vardas", "pavarde", "gimimo_metai",
                 "tautybe", "priskirtas_vilkikas"]
    )
    edited = vairuotojai_table(df, key="vairuotojai")

    if edited is not None:
        for row in edited.to_dict(orient="records"):
            update_vilkikas(conn, c, row["id"], row["priskirtas_vilkikas"])
        st.success("✅ Assignments updated")
