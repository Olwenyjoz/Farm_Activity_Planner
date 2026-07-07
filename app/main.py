from fastapi import FastAPI
from app.api.home import router as home_router
from app.api.planner import router as planner_router

app = FastAPI()

app.include_router(home_router)

app.include_router(planner_router)