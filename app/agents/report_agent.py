"""
=========================================================
Module: report_agent.py

Purpose:
    Farm Report Agent.

Responsibilities:
    - Prepare a summary of the generated farm plan.
    - Format data for frontend display.
    - Prepare content for email and PDF reports.


=========================================================
"""


class ReportAgent:
    """
    AI agent responsible for preparing farm reports.
    """

    def __init__(self):
        """
        Initialize the Report Agent.
        """
        pass

    # =====================================================
    # GENERATE REPORT
    # =====================================================

    def generate_report(
        self,
        plan: dict
    ):
        """
        Generate a summarized report from a farm plan.
        """

        report = {

            "crop": plan.get("crop"),

            "planting_date": plan.get("planting_date"),

            "weather": plan.get("weather"),

            "activities": len(
                plan.get("activities", [])
            ),

            "recommendations": len(
                plan.get("recommendations", [])
            ),

            "resource_report": plan.get(
                "resource_report"
            ),

            "status": "READY"
        }

        return report