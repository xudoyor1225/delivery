from fastapi import APIRouter

user_router = APIRouter(prefix="/users")

@user_router.get("/")
async def user_profile():
    return {"user": "Hello World"}