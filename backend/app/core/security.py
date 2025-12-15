from fastapi import Depends, HTTPException, Header
import jwt
from app.core.config import settings
from app.core.supabase_client import supabase

def get_current_user(authorization: str = Header(...)):
    try:
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(
            token,
            settings.supabase_jwt_secret,
            algorithms=["HS256"]
        )

        user_id = payload["sub"]  # Supabase user UUID

        # Fetch app user
        result = supabase.table("users") \
            .select("*") \
            .eq("user_id", user_id) \
            .single() \
            .execute()

        if not result.data:
            raise HTTPException(status_code=401, detail="User not found")

        return result.data

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
