# %%
import pandas as pd
import requests
import json

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# %%
base_url = "https://lldev.thespacedevs.com/2.2.0/launch/previous"


# %%
def get_results(url):
    response = requests.get(url)

    if "40" in response:
        print(response)
        exit()
    else:
        pass

    clean_data = json.loads(response.text)

    data = pd.json_normalize(clean_data["results"])

    data["window_start"] = pd.to_datetime(data["window_start"]).dt.round("60min")
    data["date"] = data["window_start"].dt.date
    data["time"] = data["window_start"].dt.time

    columns_to_keep = [
        "name",
        "status.name",
        "launch_service_provider.name",
        "rocket.configuration.name",
        "mission.name",
        "pad.name",
        "pad.latitude",
        "pad.longitude",
        "pad.location.name",
        "date",
        "time",
    ]

    data = data[columns_to_keep]

    data = data[data['pad.location.name'].str.contains('USA')]

    return data


# %%
# get_results(base_url)

# %%
