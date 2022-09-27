from contextlib import nullcontext as not_raises

import pytest
import src.libs.models.actual_weather as contracts
import src.libs.models.weather_reader as reader
import src.libs.models.weather_reader as saver


not_int_err = Exception("got not int")
no_data_err = Exception("don't get weather")


@pytest.mark.parametrize(
    "lan, lon, exception_check",
    [
        (30, 60, not_raises()),
        (30, 160, not_raises()),
        (15, -83, not_raises()),
    ],
)
def test_weather_api_good(lan: float, lon: float, exception_check):
    with exception_check:
        weather = reader.get_weather_by_api(lan, lon)

        if not weather:
            raise no_data_err

        if type(weather) is not int:
            raise not_int_err


@pytest.mark.parametrize(
    "lan, lon, exception_check",
    [
        (30, 1160, pytest.raises(Exception)),
        (181, 0, pytest.raises(Exception)),
        (-255, 24, pytest.raises(Exception)),
    ],
)
def test_weather_api_bad(lan: float, lon: float, exception_check):
    with exception_check:
        weather = reader.get_weather_by_api(lan, lon)

        if not weather:
            raise no_data_err

        if type(weather) is not int:
            raise not_int_err


@pytest.mark.parametrize(
    "id, exception_check",
    [
        (30, pytest.raises(Exception)),
        (181, pytest.raises(Exception)),
        (-255, pytest.raises(Exception)),
    ],
)
def test_weathether_cache_bad(id: int, exception_check):
    with exception_check:
        weather = reader.get_weather_cached(id)

        if not weather:
            raise no_data_err

        if type(weather) is not int:
            raise not_int_err


@pytest.mark.parametrize(
    "id, exception_check",
    [
        (0, pytest.raises(Exception)),
        (2, pytest.raises(Exception)),
        (1, not_raises()),
    ],
)
def test_read(id: int, exception_check):
    with exception_check:
        weather = reader.get_weather(int(id))

        if not weather:
            raise no_data_err

        if type(weather) is not int:
            raise not_int_err
