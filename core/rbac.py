from core.auth import sb_authed, require_login

def get_departamentos():
    require_login()
    sb = sb_authed()
    return sb.table("departamentos").select("id,nome").order("nome").execute().data

def get_role(departamento_id: str) -> str:
    require_login()
    sb = sb_authed()
    rows = sb.table("membros").select("role").eq("departamento_id", departamento_id).limit(1).execute().data
    return rows[0]["role"] if rows else "leitor"

def can_write(role: str) -> bool:
    return role in ("admin","operador")

