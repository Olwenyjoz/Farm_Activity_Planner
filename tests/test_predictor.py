from app.ml.predictor import CropPredictor

predictor = CropPredictor()

result = predictor.predict(
    temperature=26,
    humidity=70,
    rainfall=120,
    farm_size=5,
    soil_type="Loamy",
    season="Rainy"
)

print(result)