from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Leon AI")

app.include_router(router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Leon AI is running 🚀"}
