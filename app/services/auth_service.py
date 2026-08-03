"""
=========================================================
Module: auth_service.py

Purpose:
    Authentication business logic.

Responsibilities:
    - Register users
    - Authenticate users
    - Generate JWT tokens
    
=========================================================
"""

from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.core.security import hash_password
from app.core.security import verify_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import Token
from app.schemas.user import UserCreate
from app.schemas.user import UserLogin


class AuthService:
    """
    Authentication service.
    """

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register(
        self,
        user_data: UserCreate
    ) -> User:

        existing_user = self.repository.get_user_by_email(
            user_data.email
        )

        if existing_user:

            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists."
            )
            
        existing_phone = self.repository.get_user_by_phone(
                user_data.phone
            )

        if existing_phone:

                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Phone number already exists."
                )

        user = User(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            phone=user_data.phone,
            password_hash=hash_password(
                user_data.password
            )
        )

        return self.repository.create_user(user)

    def login(
        self,
        credentials: UserLogin
    ) -> Token:

        user = self.repository.get_user_by_email(
            credentials.email
        )

        if not user:

            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
            )

        if not verify_password(
            credentials.password,
            user.password_hash
        ):

            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
            )

        token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
                "role": user.role.value
            }
        )

        return Token(
            access_token=token
        )