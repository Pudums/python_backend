from pydantic import BaseModel


class Region(BaseModel):
    """
        id - id of region where is wheather
        real_weather - what is real temperature
        """

        id: int
        real_weather: int | None
        token: str
