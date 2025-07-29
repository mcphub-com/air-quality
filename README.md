# Air Quality MCP Server

## Overview

The 'air-quality' MCP server is designed to provide comprehensive air quality information for any location worldwide. This server delivers current, forecasted, and historical air quality data, allowing users to monitor and analyze air quality conditions effectively.

## Features

- **Current Air Quality**: Retrieve real-time air quality conditions, including detailed pollutant concentrations and pollen levels, for any specified location.
- **Air Quality Forecast**: Obtain a 3-day (72-hour) air quality forecast to anticipate changes and plan accordingly.
- **Air Quality History**: Access data from the past 24 hours to understand air quality trends and anomalies.

## Data Fields

### Current Air Quality

- **Location Information**:
  - `lat`: Latitude (Degrees)
  - `lon`: Longitude (Degrees)
  - `timezone`: Local IANA Timezone
  - `city_name`: Nearest city name
  - `country_code`: Country abbreviation
  - `state_code`: State abbreviation/code

- **Pollutant Concentrations**:
  - `aqi`: Air Quality Index [US - EPA standard 0 - +500]
  - `o3`: Ozone (µg/m³)
  - `so2`: Sulfur Dioxide (µg/m³)
  - `no2`: Nitrogen Dioxide (µg/m³)
  - `co`: Carbon Monoxide (µg/m³)
  - `pm25`: Particulate Matter < 2.5 microns (µg/m³)
  - `pm10`: Particulate Matter < 10 microns (µg/m³)

- **Pollen Levels**:
  - `pollen_level_tree`: Tree pollen level (0 = None, 1 = Low, 2 = Moderate, 3 = High, 4 = Very High)
  - `pollen_level_grass`: Grass pollen level (0 = None, 1 = Low, 2 = Moderate, 3 = High, 4 = Very High)
  - `pollen_level_weed`: Weed pollen level (0 = None, 1 = Low, 2 = Moderate, 3 = High, 4 = Very High)
  - `mold_level`: Mold pollen level (0 = None, 1 = Low, 2 = Moderate, 3 = High, 4 = Very High)
  - `predominant_pollen_type`: Predominant pollen type (Trees/Weeds/Molds/Grasses)

### Historical Air Quality

- **Timestamps**:
  - `timestamp_local`: Local time
  - `timestamp_utc`: UTC time
  - `ts`: Unix Timestamp at UTC time

- **Pollutant Concentrations**: Same as Current Air Quality

### Forecast Air Quality

- **Timestamps**: Same as Historical Air Quality
- **Pollutant Concentrations**: Same as Current Air Quality

## Tool List

1. **Air Quality History**: Returns the past 24 hours of air quality observations for any location given latitude and longitude.

2. **Air Quality Forecast**: Provides a 3-day air quality forecast for any location given latitude and longitude.

3. **Current Air Quality**: Retrieves current air quality conditions for any location given latitude and longitude.

## Tool Declarations

- **air_quality_history**
  - **Description**: Returns the past 24 hours of air quality observations.
  - **Parameters**:
    - `lon` (Number): Longitude
    - `lat` (Number): Latitude

- **air_quality_forecast**
  - **Description**: Provides a 3-day air quality forecast.
  - **Parameters**:
    - `lat` (Number): Latitude
    - `lon` (Number): Longitude
    - `hours` (Number, optional): Limits response forecast hours (default 72)

- **current_air_quality**
  - **Description**: Retrieves current air quality conditions.
  - **Parameters**:
    - `lon` (String): Longitude
    - `lat` (String): Latitude

This README serves as a guide to understanding and utilizing the 'air-quality' MCP server for monitoring air quality conditions worldwide.