"""
=========================================================
Module: farm_exceptions.py

Purpose:
    Defines custom exceptions used throughout the
    Farm Activity Planner AI.

Responsibilities:
    - Provide meaningful application-specific errors
    - Improve readability
    - Centralize exception handling

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from fastapi import HTTPException


class CropNotSupportedError(HTTPException):
    """
    Raised when the requested crop is not supported
    by the planner.
    """

    def __init__(self, crop_name: str):

        super().__init__(
            status_code=400,
            detail=f"Crop '{crop_name}' is not supported."
        )