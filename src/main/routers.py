from fastapi import APIRouter
from starlette.responses import RedirectResponse
import starlette.status as status
import src.libs.models.item as contracts
import random
import time

router = APIRouter()


@router.get("/")
def read_root():
    return {"Description": "Some description of this service"}


@router.get("/region/{region_id}")
async def read_weather(region_id: int):
    return {"weather_ is": "good", "chance_of_rain_is": 15, "region_id": region_id}


@router.get("/random_region/")
async def read_random_region_data():
    return RedirectResponse(f"/region/{int(random.random() * 100)}")


@ router.post("/add_real_weather/")
async def save_data(item: contracts.Region):
    item_dict = item.dict()

    is_ok = await save_data()

    item_dict.update({"save_status": is_ok})

    return item_dict


async def save_data():
    time.sleep(random.random() / 2)
    return True