from fastapi import FastAPI
import uvicorn
from user_rotes import user_router
from zakaz_routs import zakaz_router


app = FastAPI()
app.include_router(user_router)
app.include_router(zakaz_router)



@app.get("/")
async def root():
    return {"messages": "Bu yetkazib berish web sahifasining Api"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000,host="127.0.0.1")