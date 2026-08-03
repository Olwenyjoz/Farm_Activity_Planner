from app.ml.recommendation_service import RecommendationService

service = RecommendationService()

result = service.recommend_crop(

    temperature=26,

    humidity=70,

    rainfall=120,

    farm_size=5,

    soil_type="Loamy",

    season="Rainy"
)

print(result)