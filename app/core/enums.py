"""
=========================================================
Module: enums.py

Purpose:
    Defines all application-wide enumerations (Enums)
    used throughout the Farm Activity Planner AI.

Why Enums?
    - Prevent spelling mistakes
    - Improve readability
    - Centralize shared values
    - Simplify maintenance
    - Enable IDE auto-completion

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from enum import Enum


class RecommendationSeverity(str, Enum):
    """
    Represents the severity level of a recommendation.
    """

    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    
class RecommendationCategory(str, Enum):
    """
    Represents the category of a recommendation.
    """

    WORKERS = "Workers"
    WEATHER = "Weather"
    PRIORITY = "Priority"