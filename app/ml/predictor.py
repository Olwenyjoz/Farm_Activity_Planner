"""
=========================================================
Module: predictor.py

Purpose:
    Crop recommendation prediction engine.

Responsibilities:
    - Load the trained machine learning model.
    - Load feature encoders.
    - Encode user input.
    - Predict the most suitable crop.
    - Return prediction confidence.

=========================================================
"""

from pathlib import Path

import joblib
import pandas as pd


class CropPredictor:
    """
    Machine Learning prediction engine.
    """

    def __init__(self):
        """
        Load the trained model and encoders.
        """

        base_dir = Path(__file__).resolve().parent

        self.model = joblib.load(
            base_dir / "crop_model.pkl"
        )

        self.soil_encoder = joblib.load(
            base_dir / "soil_encoder.pkl"
        )

        self.season_encoder = joblib.load(
            base_dir / "season_encoder.pkl"
        )

        self.crop_encoder = joblib.load(
            base_dir / "crop_encoder.pkl"
        )

    # =====================================================
    # PREDICT CROP
    # =====================================================

    def predict(
        self,
        temperature: float,
        humidity: float,
        rainfall: float,
        farm_size: float,
        soil_type: str,
        season: str
    ):
        """
        Predict the most suitable crop.

        Workflow:
            1. Encode categorical features.
            2. Prepare feature vector.
            3. Predict crop.
            4. Calculate confidence.
            5. Return prediction.
        """

        # ---------------------------------------------
        # Encode categorical values
        # ---------------------------------------------

        soil = self.soil_encoder.transform(
            [soil_type]
        )[0]

        season = self.season_encoder.transform(
            [season]
        )[0]

        # ---------------------------------------------
        # Create feature dataframe
        # ---------------------------------------------

        features = pd.DataFrame(
            [[
                temperature,
                humidity,
                rainfall,
                farm_size,
                soil,
                season
            ]],
            columns=[
                "temperature",
                "humidity",
                "rainfall",
                "farm_size",
                "soil_type",
                "season"
            ]
        )

        # ---------------------------------------------
        # Predict crop
        # ---------------------------------------------

        prediction = self.model.predict(
            features
        )[0]

        probabilities = self.model.predict_proba(
            features
        )[0]

        confidence = max(probabilities) * 100

        crop = self.crop_encoder.inverse_transform(
            [prediction]
        )[0]

        # ---------------------------------------------
        # Return result
        # ---------------------------------------------

        return {

            "recommended_crop": crop,

            "confidence": round(
                confidence,
                2
            ),

            "message": (
                f"{crop} is the most suitable crop "
                f"for the provided conditions."
            )
        }