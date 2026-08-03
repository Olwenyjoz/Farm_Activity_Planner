"""
=========================================================
Module: user_repository.py

Purpose:
    Handles all database operations related to users.

Responsibilities:
    - Create users
    - Retrieve users
    - Update users
    - Delete users

=========================================================
"""

from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    """
    Repository class for user database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User) -> User:
        """
        Save a new user.
        """
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def get_user_by_id(self, user_id: int) -> User | None:
        """
        Retrieve a user by ID.
        """
        return (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def get_user_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by email.
        """
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_all_users(self) -> list[User]:
        """
        Retrieve all users.
        """
        return (
            self.db.query(User)
            .order_by(User.id)
            .all()
        )

    def update_user(self, user: User) -> User:
        """
        Update an existing user.
        """
        self.db.commit()
        self.db.refresh(user)

        return user

    def delete_user(self, user: User) -> None:
        """
        Delete a user.
        """
        self.db.delete(user)
        self.db.commit()
        
        
    def get_user_by_phone(
        self,
        phone: str
    ):
        return (
            self.db.query(User)
            .filter(User.phone == phone)
            .first()
        )