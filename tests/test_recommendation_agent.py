from app.agents.recommendation_agent import RecommendationAgent

agent = RecommendationAgent()

result = agent.recommend(

    temperature=26,

    humidity=70,

    rainfall=120,

    farm_size=5,

    soil_type="Loamy",

    season="Rainy"
)

print(result)