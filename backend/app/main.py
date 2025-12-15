from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.landing.router import router as landing_router
from app.admin.courses_router import router as admin_courses_router



app = FastAPI(title="Academy Backend")

app.include_router(auth_router)
app.include_router(landing_router)
app.include_router(admin_courses_router)
