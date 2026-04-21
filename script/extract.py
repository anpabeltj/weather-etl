import requests

def get_coordinates(city_name):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
    response = requests.get(url) 
    data = response.json()
    lat = data["results"][0]["latitude"]
    long = data["results"][0]["longitude"]
    return [lat, long]


def extract_city(city_name):

    lat, long = get_coordinates(city_name)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": long,
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
        "timezone": "Asia/Jakarta",
        "past_days": 7
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    result = extract_city("Jakarta")
    print(result)