"""
=========================================================
Module: role.py

Purpose:
    Defines user roles for authorization.

=========================================================
"""

from enum import Enum


class UserRole(str, Enum):
    """
    User roles within the system.
    """

    ADMIN = "ADMIN"
    FARMER = "FARMER"