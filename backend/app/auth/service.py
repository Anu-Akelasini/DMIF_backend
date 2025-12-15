from app.core.supabase_client import supabase

def register_user(name: str, email: str, password: str):
    # 1. Create auth user
    result = supabase.auth.sign_up({
        "email": email,
        "password": password
    })

    # 2. Update users table with name
    if result.user:
        supabase.table("users").update({
            "name": name
        }).eq("user_id", result.user.id).execute()

    return result


def login_user(email: str, password: str):
    return supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })
