"""
=========================================================
Module: date_utils.py

Purpose:
    Provides reusable date helper functions for the
    Farm Activity Planner AI.

Responsibilities:
    - Format dates
    - Perform reusable date conversions
    - Keep date logic centralized

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import date


def format_date(date_value: date) -> str:
    """
    Convert a Python date object into a readable format.

    Parameters
    ----------
    date_value : date
        The date to format.

    Returns
    -------
    str
        Formatted date string.

    Example
    -------
    2026-07-15

    becomes

    15 Jul 2026
    """

    return date_value.strftime("%d %b %Y")