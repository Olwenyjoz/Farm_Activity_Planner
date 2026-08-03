from app.clients.weather_client import WeatherClient

client = WeatherClient()

weather = client.get_weather(
    latitude=-1.286389,
    longitude=36.817223
)

print(weather)