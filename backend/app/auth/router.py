from fastapi import APIRouter
from app.auth.service import register_user, login_user
from app.models.schemas import RegisterRequest, LoginRequest

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(payload: RegisterRequest):
    return register_user(
        name=payload.name,
        email=payload.email,
        password=payload.password
    )

@router.post("/login")
def login(payload: LoginRequest):
    return login_user(payload.email, payload.password)
