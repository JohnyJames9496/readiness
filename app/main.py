from fastapi import FastAPI
from app.api.scoring import router

app = FastAPI(title="Internship Readiness API")
app.include_router(router)
