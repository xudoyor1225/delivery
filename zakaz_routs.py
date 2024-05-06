from fastapi import APIRouter

zakaz_router = APIRouter(prefix="/zakaz")

@zakaz_router.get("/")
async def zakaz_profile():
    return {"message": "Zakaz Profile API"}