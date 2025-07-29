import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/weatherbit/api/air-quality'

mcp = FastMCP('air-quality')

@mcp.tool()
def air_quality_history(lon: Annotated[Union[int, float], Field(description='Longitude Default: -78.638')],
                        lat: Annotated[Union[int, float], Field(description='Latitude Default: 35.779')]) -> dict: 
    '''Returns the past 24 hours of air quality observations for any point in the world given a lat/lon.'''
    url = 'https://air-quality.p.rapidapi.com/history/airquality'
    headers = {'x-rapidapi-host': 'air-quality.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lon': lon,
        'lat': lat,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def air_quality_forecast(lat: Annotated[Union[int, float], Field(description='Latitude Default: 35.779')],
                         lon: Annotated[Union[int, float], Field(description='Longitude Default: -78.638')],
                         hours: Annotated[Union[int, float, None], Field(description='Limits response forecast hours (default 72). Default: 72')] = None) -> dict: 
    '''Returns a 3 day (72 hour) air quality forecast for any point in the world given a lat/lon.'''
    url = 'https://air-quality.p.rapidapi.com/forecast/airquality'
    headers = {'x-rapidapi-host': 'air-quality.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat': lat,
        'lon': lon,
        'hours': hours,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def current_air_quality(lon: Annotated[str, Field(description='Longitude')],
                        lat: Annotated[str, Field(description='Latitude')]) -> dict: 
    '''Retrieves current air quality conditions for any location in the world, given a lat/lon.'''
    url = 'https://air-quality.p.rapidapi.com/current/airquality'
    headers = {'x-rapidapi-host': 'air-quality.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lon': lon,
        'lat': lat,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
