# %%
import pandas as pd
import requests
import json

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# %%
base_url = "https://api.weather.gov/"

# %% [markdown]
# ***


# %%
def get_weather(base_url, lat, lon, dt, tm):
    day_filter = dt
    time_filter = tm

    forecast = requests.get(base_url + "points/{},{}".format(lat, lon))

    if "40" in forecast:
        print(forecast)
        exit()
    else:
        pass

    forecast_json = json.loads(forecast.text)

    forecast_properties = pd.json_normalize(forecast_json["properties"])
    properties = requests.get(forecast_properties["forecastHourly"][0])
    properties_json = json.loads(properties.text)

    periods = pd.json_normalize(properties_json["properties"])
    periods_data = pd.json_normalize(periods["periods"][0])

    periods_data = periods_data[periods_data["startTime"].str.contains(str(day_filter))]

    periods_data = periods_data[
        periods_data["startTime"].str.contains(str(time_filter))
    ]

    periods_data["Temperature"] = periods_data[
        ["temperature", "temperatureUnit"]
    ].apply(lambda row: " ".join(row.values.astype(str)), axis=1)

    periods_data["Wind"] = periods_data[["windSpeed", "windDirection"]].apply(
        lambda row: " ".join(row.values.astype(str)), axis=1
    )

    columns_to_keep = [
        "Temperature",
        "Wind",
        "shortForecast",
        "probabilityOfPrecipitation.value",
        "dewpoint.value",
        "relativeHumidity.value",
    ]
    periods_data = periods_data[columns_to_keep]

    periods_data = periods_data.rename(
        columns={
            "shortForecast": "Forecast",
            "probabilityOfPrecipitation.value": "Chance of Precipitation",
            "dewpoint.value": "Dewpoint",
            "relativeHumidity.value": "Humidity",
        }
    )

    return periods_data


# %% [markdown]
# ***

# %% [markdown]
# Cape Canaveral, FL, USA

# %%
# Starlink Group 6-11
# get_weather(base_url, 28.561941, -80.577357, '2023-08-23', '00:00:00')

# %%
# Starlink Group 7-1
# get_weather(base_url, 28.561941, -80.577357, '2023-08-22', '06:00:00')
