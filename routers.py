from fastapi import APIRouter
import item as contracts

router = APIRouter()


@router.get("/")
def read_root():
    return {"Description": "Some description of this service"}


@router.get("/region/{region_id}")
async def read_item(region_id: int):
    return {"weather_ is": "good", "chance_of_rain_is": 15}


@router.get("/user/")
async def read_user(user_id: str, q: str | None = None):
    if q:
        return {"user_id": user_id, "q": q}
    return {"user_id": user_id}


@router.post("/items/")
async def create_item(item: contracts.Item):
    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
