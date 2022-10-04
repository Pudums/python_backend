import src.libs.models.actual_weather as contracts
import requests
import json
import time

id_to_ll = {
    1: (60.03, 30.33)
}


cached = {
}


def get_weather_by_api(lat: float, lon: float):
    data = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")

    if data.status_code != 200:
        return

    content_json = json.loads(str(data.content)[2:-1])

    return int(content_json["current_weather"]["temperature"])


def get_weather_cached(id: int):
    data = cached.get(id)
    if not data:
        return

    if time.time() - data[1] > 3600:
        cached.pop(id)
        return

    return data[0]


def get_weather(id: int):
    weather = get_weather_cached(id)
    if weather:
        return weather

    lan, lon = id_to_ll[id]
    if not lan:
        return

    return get_weather_by_api(lan, lon)


def read(id: int):
    if not id or type(id) is not int or id <= 0:
        return
    weather = get_weather(id)

    if not weather:
        return

    return {"region_id": id,
            "weather": weather,
            }


def save(item: contracts.Region):
    if not item.real_weather:
        return False

    cached[item.id] = (item.real_weather, time.time())
    return True
