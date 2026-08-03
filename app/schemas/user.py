"""
=========================================================
Module: user.py

Purpose:
    Pydantic schemas for user authentication.

Responsibilities:
    - User registration
    - User login
    - User responses
    - JWT token responses


=========================================================
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr


class UserCreate(BaseModel):
    """
    User registration schema.
    """

    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None
    password: str
    role: str = "FARMER"


class UserLogin(BaseModel):
    """
    User login schema.
    """

    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """
    User response schema.
    """

    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None
    role: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class Token(BaseModel):
    """
    JWT token response.
    """

    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """
    JWT payload.
    """

    user_id: int
    email: EmailStr
    role: str