import streamlit as st
from core.supabase_client import get_supabase

def auth_init():
    st.session_state.setdefault("access_token", None)
    st.session_state.setdefault("user", None)
    st.session_state.setdefault("departamento_id", None)

def sign_in(email: str, password: str):
    sb = get_supabase()
    res = sb.auth.sign_in_with_password({"email": email, "password": password})
    st.session_state["access_token"] = res.session.access_token
    st.session_state["user"] = res.user

def sign_up(email: str, password: str):
    sb = get_supabase()
    sb.auth.sign_up({"email": email, "password": password})

def sign_out():
    sb = get_supabase()
    try:
        sb.auth.sign_out()
    except Exception:
        pass
    for k in ["access_token", "user", "departamento_id"]:
        st.session_state[k] = None

def require_login():
    if not st.session_state.get("access_token"):
        st.error("Você precisa estar logado.")
        st.stop()

def sb_authed():
    sb = get_supabase()
    token = st.session_state.get("access_token")
    if token:
        sb.postgrest.auth(token)
        sb.storage.auth(token)
    return sb

