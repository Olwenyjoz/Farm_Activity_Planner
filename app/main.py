"""
=========================================================
Module: main.py

Purpose:
    Entry point for the Farm Activity Planner AI API.

Responsibilities:
    - Create the FastAPI application.
    - Configure CORS.
    - Initialize database tables.
    - Register API routers.


Project:
    Farm Activity Planner AI
=========================================================
"""
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.home import router as home_router
from app.api.planner import router as planner_router

from app.database.base import Base
from app.database.connection import engine

# Import ORM models
from app.database.models import FarmPlanModel
from app.models.user import User

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Farm Activity Planner AI",
    version="1.0.0",
    description="AI-powered farm activity planning system."
)

# ==========================================
# CORS Configuration
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# Register Routers
# =====================================================

app.include_router(home_router)
app.include_router(auth_router)
app.include_router(planner_router)