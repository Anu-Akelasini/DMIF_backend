from fastapi import APIRouter, Depends
from app.core.roles import require_admin

router = APIRouter(
    prefix="/admin/courses",
    tags=["Admin Courses"]
)

@router.post("/")
def create_course(course: dict, admin=Depends(require_admin)):
    return {
        "message": "Course created",
        "created_by": admin["email"]
    }
