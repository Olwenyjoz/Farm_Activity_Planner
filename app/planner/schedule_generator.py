"""
=========================================================
Module: schedule_generator.py

Purpose:
    Generates a complete farm activity schedule based on
    the selected crop and planting date.

Responsibilities:
    - Validate the requested crop
    - Generate activity dates
    - Generate resource requirements
    - Detect worker conflicts
    - Generate intelligent recommendations
    - Return the complete farm plan

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from fastapi import HTTPException

from app.schemas.farm_plan import FarmPlanRequest

from app.planner.crop_rules import CROP_RULES
from app.planner.resource_allocator import generate_resource_report
from app.planner.conflict_detector import detect_worker_conflicts
from app.planner.decision_engine import generate_recommendations
from app.planner.calendar.generator import generate_calendar

from app.core.logger import logger
from app.exceptions.farm_exceptions import CropNotSupportedError


def generate_schedule(request: FarmPlanRequest):
    """
    Generate a complete farm activity schedule.

    Parameters
    ----------
    request : FarmPlanRequest
        The validated farm planning request received
        from the API.

    Returns
    -------
    dict
        A complete farm plan containing:
        - Crop information
        - Scheduled activities
        - Resource report
        - Worker conflicts
        - Recommendations

    Raises
    ------
    HTTPException
        If the requested crop is not supported.
    """

    # =====================================================
    # Start Schedule Generation
    # =====================================================
    logger.info(
        f"Generating farm schedule for crop '{request.crop}'."
    )

    # =====================================================
    # Retrieve Crop Rules
    # =====================================================
    rules = CROP_RULES.get(request.crop)

    if rules is None:

        logger.warning(
            f"Unsupported crop requested: '{request.crop}'."
        )

        raise CropNotSupportedError(request.crop)

    # =====================================================
    # Generate Activity Schedule
    # =====================================================
    activities = []

    for activity in rules["activities"]:

        # Calculate the activity date by adding the
        # configured offset to the planting date.
        activity_date = (
            request.planting_date + activity["offset"]
        )

        activities.append(
            {
                **activity,
                "date": activity_date
            }
        )

    # =====================================================
    # Build Schedule Object
    # =====================================================
    schedule = {
        "crop": request.crop,
        "planting_date": request.planting_date,
        "activities": activities,
    }

    # =====================================================
    # Generate Resource Report
    # =====================================================
    resource_report = generate_resource_report(schedule)

    # =====================================================
    # Detect Worker Conflicts
    # =====================================================
    conflicts = detect_worker_conflicts(
        schedule,
        request.workers
    )

    # =====================================================
    # Generate Recommendations
    # =====================================================
    recommendations = generate_recommendations(
        schedule,
        resource_report,
        conflicts
    )
    
    # =====================================================
    # Generate Calendar Events
    # =====================================================
    logger.info(
    "Generating calendar events."
    )

    calendar = generate_calendar(schedule)

    # =====================================================
    # Schedule Generation Completed
    # =====================================================
    logger.info(
        "Farm schedule generated successfully."
    )
    
    logger.info(
    f"Generated {len(calendar)} calendar event(s)."
    )
    
    # =====================================================
    # Return Complete Farm Plan
    # =====================================================
    return {
    **schedule,
    "resource_report": resource_report,
    "conflicts": conflicts,
    "recommendations": recommendations,
    "calendar": calendar,
    }