"""
=========================================================
Module: text_utils.py

Purpose:
    Provides reusable text formatting functions.

Responsibilities:
    - Format lists
    - Standardize text output
    - Improve readability

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""


def format_activity_list(activities: list[str]) -> str:
    """
    Convert a list of activity names into a readable string.

    Example
    -------
    ["Harvest", "Packaging"]

    becomes

    "Harvest, Packaging"
    """

    return " • ".join(activities)