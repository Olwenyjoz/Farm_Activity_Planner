"""
=========================================================
Module: auth.py

Purpose:
    Authentication API endpoints.

Responsibilities:
    - User registration
    - User login

=========================================================
"""

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import Token
from app.schemas.user import UserCreate
from app.schemas.user import UserResponse
from app.schemas.user import UserLogin
from app.services.auth_service import AuthService

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Register a new user.
    """
    service = AuthService(db)

    return service.register(user)


@router.post(
    "/login",
    response_model=Token
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Authenticate a user.
    """

    service = AuthService(db)

    credentials = UserLogin(
        email=form_data.username,
        password=form_data.password
    )

    return service.login(credentials)