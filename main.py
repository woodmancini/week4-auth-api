from fastapi import FastAPI

import models
from database import engine
from routers import auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth")

@app.get("/")
def home():
    return {"message":"Week 4 auth API is running"}