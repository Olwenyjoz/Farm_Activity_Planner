"""
=========================================================
Module: logger.py

Purpose:
    Configure application-wide logging for the
    Farm Activity Planner AI.

Responsibilities:
    - Configure log format
    - Define log level
    - Provide reusable logger instances

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

import logging

# Configure the root logger
logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(message)s"
    ),
)

# Create a reusable application logger
logger = logging.getLogger("FarmActivityPlanner")