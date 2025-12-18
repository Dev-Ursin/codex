import streamlit as st
import pandas as pd
from core.auth import require_login, sb_authed

st.set_page_config(page_title="Auditoria", layout="wide")
require_login()

dep_id = st.session_state.get("departamento_id")
if not dep_id:
    st.error("Selecione um departamento na Home.")
    st.stop()

sb = sb_authed()
st.title("🧾 Auditoria / Logs (Imutáveis)")

limite = st.number_input("Limite", 50, 5000, 300, 50)
rows = sb.table("audit_log") \
    .select("at,action,table_name,record_id,actor_email,actor_user_id") \
    .eq("departamento_id", dep_id) \
    .order("at", desc=True) \
    .limit(int(limite)) \
    .execute().data

df = pd.DataFrame(rows) if rows else pd.DataFrame()
st.dataframe(df, use_container_width=True, hide_index=True)

st.caption("Esses logs são append-only no banco: sem UPDATE/DELETE.")

