from supabase import create_client
from app.core.config import settings

supabase = create_client(
    settings.supabase_url,
    settings.supabase_anon_key
)
