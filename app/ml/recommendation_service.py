"""
=========================================================
Module: recommendation_service.py

Purpose:
    Crop recommendation service powered by
    Machine Learning.

Responsibilities:
    - Connect FastAPI services with the
      trained ML model.
    - Generate crop recommendations.
    - Produce AI explanations.


=========================================================
"""

from app.ml.predictor import CropPredictor


class RecommendationService:
    """
    Service responsible for generating
    AI-powered crop recommendations.
    """

    def __init__(self):
        """
        Initialize the predictor.
        """

        self.predictor = CropPredictor()

    # =====================================================
    # RECOMMEND CROP
    # =====================================================

    def recommend_crop(
        self,
        temperature: float,
        humidity: float,
        rainfall: float,
        farm_size: float,
        soil_type: str,
        season: str
    ):
        """
        Generate a crop recommendation using
        the trained machine learning model.

        Workflow:
            1. Receive environmental conditions.
            2. Pass data to the predictor.
            3. Receive prediction.
            4. Return AI recommendation.
        """

        prediction = self.predictor.predict(

            temperature=temperature,

            humidity=humidity,

            rainfall=rainfall,

            farm_size=farm_size,

            soil_type=soil_type,

            season=season
        )

        return prediction