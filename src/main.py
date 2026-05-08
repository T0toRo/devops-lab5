from fastapi import FastAPI

from src.routers.user import router as user_router

app = FastAPI(title="DevOps Lab 5 App")

app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "DevOps Lab 5 CI/CD app"}
