from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        weather_description = weather_data["weather"][0]["description"]

        return {
            "temperature": temperature,
            "humidity": humidity,
            "description": weather_description,
        }
    else:
        return {"error": "City not found"}

def weather_view(request):
    api_key = "593e448f974d0949b16c11fd96bb3599"  # Replace with your OpenWeatherMap API key
    city = request.GET.get("city", "Warangal")  # Default to London if city not provided

    weather_info = get_weather(api_key, city)

    context = {"city": city, "weather_info": weather_info}
    return render(request, "weather_app/weather.html", context)
