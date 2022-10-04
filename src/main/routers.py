from fastapi import APIRouter, HTTPException
from starlette.responses import RedirectResponse
import starlette.status as status
import src.libs.models.actual_weather as contracts
import src.libs.models.weather_reader as reader
import src.libs.models.weather_reader as saver
import random
import time

router = APIRouter()


err_region_not_found = """
    Region id not found. U can add real weather by handler /add_real_weather/
"""


@router.get("/")
def read_root():
    return {"Description": "imagine link to github readme of this project (it will be when HW2 will merged)"}


@router.get("/region/{region_id}")
async def read_weather(region_id: int):
    res = reader.read(region_id)
    if not res:
        raise HTTPException(status_code=404, detail=err_region_not_found)
    return res


@router.get("/random_region/")
async def read_random_region_data():
    return RedirectResponse(f"/region/{int(random.random() * 100)}")


@ router.post("/add_real_weather/")
async def save_data(item: contracts.Region):
    item_dict = item.dict()

    is_ok = saver.save(item)

    item_dict.update({"save_status": is_ok})

    return item_dict
