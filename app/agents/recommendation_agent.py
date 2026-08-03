"""
=========================================================
Module: recommendation_agent.py

Purpose:
    Crop Recommendation Agent.

Responsibilities:
    - Coordinate crop recommendation.
    - Invoke the Machine Learning recommendation service.
    - Produce AI-powered crop recommendations.
    - Return prediction confidence and explanation.


=========================================================
"""

from app.ml.recommendation_service import RecommendationService


class RecommendationAgent:
    """
    AI agent responsible for crop recommendation.
    """

    def __init__(self):
        """
        Initialize the Recommendation Service.
        """

        self.recommendation_service = RecommendationService()

    # =====================================================
    # RECOMMEND CROP
    # =====================================================

    def recommend(
        self,
        temperature: float,
        humidity: float,
        rainfall: float,
        farm_size: float,
        soil_type: str,
        season: str
    ):
        """
        Generate an AI-powered crop recommendation.

        Workflow:
            1. Receive environmental conditions.
            2. Invoke the ML recommendation service.
            3. Return the prediction.
        """

        prediction = self.recommendation_service.recommend_crop(

            temperature=temperature,

            humidity=humidity,

            rainfall=rainfall,

            farm_size=farm_size,

            soil_type=soil_type,

            season=season
        )

        return prediction