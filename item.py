from pydantic import BaseModel


class Region(BaseModel):
    """Contract for item"""

    id: int
    real_weather: str | None
