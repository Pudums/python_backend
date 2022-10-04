import grpc
import time
import random
import src.libs.models.weather_reader as saver
import src.libs.models.weather_reader as reader
import src.libs.models.actual_weather as contracts
import starlette.status as status
from fastapi import APIRouter, HTTPException
from starlette.responses import RedirectResponse
#from src.server.server_pb2_grpc import WebBackStub
#from src.server.server_pb2 import Data

import src.server as sr


router = APIRouter()


err_region_not_found = """
    Region id not found. U can add real weather by handler /add_real_weather/
"""


@router.get("/")
def read_root():
    """
    return main page/some info about service
    """
    return {"Description": "imagine link to github readme of this project (it will be when HW2 will merged)"}


@router.get("/region/{region_id}")
async def read_weather(region_id: int):
    """
    input:
        region id

    return:
        weather in region
    """
    res = reader.read(region_id)
    if not res:
        raise HTTPException(status_code=404, detail=err_region_not_found)
    return res


@router.get("/random_region/")
async def read_random_region_data():
    """
    return:
        random region weather)
    """
    return RedirectResponse(f"/region/{int(random.random() * 100)}")


@ router.post("/add_real_weather/")
async def save_data(item: contracts.Region):
    """
    input:
        token, region id, weather in region


    method tring to save weather

    return:
        is save succed

    """
    item_dict = item.dict()

    with grpc.insecure_channel("localhost:3000") as channel:
        client = sr.WebBackStub(channel)

        confirmation = client.AddWeather(sr.Data(
            token=item.token if item.token else "base_token",
            ID=item.id,
            real_weather=item.real_weather,
        ))

        print(confirmation.succed)

    item_dict.update({"save_status": is_ok})

    return item_dict
