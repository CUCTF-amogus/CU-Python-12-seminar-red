from dataclasses import dataclass
from dotenv import load_dotenv

from config.base import getenv


@dataclass
class AccuWeatherAPI:
    api_key: str
    location_url: str
    weather_url: str


@dataclass
class Config:
    api: AccuWeatherAPI


def load_config() -> Config:
    load_dotenv()
    config = Config(
        api=AccuWeatherAPI(
            api_key=getenv("API_KEY"),
            location_url=getenv("LOCATION_URL"),
            weather_url=getenv("WEATHER_URL"),
            ),
    )
    return config


config = load_config()
