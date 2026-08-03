from app.agents.weather_agent import WeatherAgent

agent = WeatherAgent()

weather = agent.analyze(

    latitude=-1.286389,

    longitude=36.817223
)

print(weather)