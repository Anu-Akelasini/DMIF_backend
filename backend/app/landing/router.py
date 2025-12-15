from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.landing.service import get_landing_page_data

router = APIRouter(
    prefix="/landing",
    tags=["Landing"]
)

@router.get("/")
def landing_page(user=Depends(get_current_user)):
    return {
        "user": {
            "email": user["email"],
            "role": user["role"]
        },
        "content": get_landing_page_data()
    }
