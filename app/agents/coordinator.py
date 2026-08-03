"""
=========================================================
Module: coordinator.py

Purpose:
    Multi-Agent Coordinator.

Responsibilities:
    - Coordinate all AI agents.
    - Execute the intelligent planning workflow.
    - Produce one optimized farm plan.


=========================================================
"""

from app.agents.weather_agent import WeatherAgent
from app.agents.recommendation_agent import RecommendationAgent
from app.agents.planner_agent import PlannerAgent
from app.agents.optimization_agent import OptimizationAgent
from app.agents.report_agent import ReportAgent


class Coordinator:
    """
    Coordinates all AI agents.
    """

    def __init__(self):
        """
        Initialize all agents.
        """

        self.weather_agent = WeatherAgent()

        self.recommendation_agent = RecommendationAgent()

        self.planner_agent = PlannerAgent()

        self.optimization_agent = OptimizationAgent()

        self.report_agent = ReportAgent()

    # =====================================================
    # EXECUTE
    # =====================================================

    def execute(
        self,
        request
    ):
        """
        Execute the complete planning workflow.
        """

        # -----------------------------------------
        # Weather
        # -----------------------------------------

        weather = self.weather_agent.analyze(

            latitude=request.latitude,

            longitude=request.longitude
        )

        # -----------------------------------------
        # Crop Recommendation
        # -----------------------------------------

        recommendation = self.recommendation_agent.recommend(

            temperature=weather["temperature"],

            humidity=weather["humidity"],

            rainfall=weather["rain"],

            farm_size=request.farm_size,

            soil_type=request.soil_type,

            season=request.season
        )

        # -----------------------------------------
        # Planner
        # -----------------------------------------

        plan = self.planner_agent.generate_plan(
            request
        )

        # Attach weather

        plan["weather"] = weather

        # Add AI recommendation

        recommendations = plan.get(
            "recommendations",
            []
        )

        recommendations.append({

            "title": "AI Crop Recommendation",

            "category": "Artificial Intelligence",

            "severity": "INFO",

            "activity": "Planning",

            "date": plan["planting_date"],

            "reason":
                f"Recommended crop: "
                f"{recommendation['recommended_crop']} "
                f"({recommendation['confidence']}%).",

            "suggested_action":
                recommendation["message"]
        })

        plan["recommendations"] = recommendations

        # -----------------------------------------
        # Optimization
        # -----------------------------------------

        plan = self.optimization_agent.optimize(
            plan
        )

        # -----------------------------------------
        # Report
        # -----------------------------------------

        report = self.report_agent.generate_report(
            plan
        )

        plan["report"] = report

        return plan