import pandas as pd
from weather import get_weather
from rocket_launch_data import get_results
from tabulate import tabulate
import os

os.system("cls")

weather_url = "https://api.weather.gov/"
rocket_launch_data_url = "https://lldev.thespacedevs.com/2.2.0/launch/upcoming"

rocket_launch = get_results(rocket_launch_data_url)

rocket_launch_data = pd.DataFrame(rocket_launch).reset_index().drop("index", axis=1)

rocket_launch_data['key'] = rocket_launch_data.index

rocket_launch_data["Launch Date"] = rocket_launch_data["Launch Date"].astype(str)
rocket_launch_data["Launch Time"] = rocket_launch_data["Launch Time"].astype(str)

weather_data = pd.DataFrame()

for i in rocket_launch_data.index:
    weather = get_weather(
        weather_url,
        rocket_launch_data["Latitude"][i],
        rocket_launch_data["Longitude"][i],
        (rocket_launch_data["Launch Date"][i]),
        (rocket_launch_data["Launch Time"][i]),
    )

    weather["key"] = i

    weather_data = pd.concat([weather_data, weather])

launch_data = pd.merge(rocket_launch_data, weather_data, how="left", on="key")

launch_data = launch_data.drop(columns=["key"], axis=1)

print(
    "Weather Data for Next {} Rocket Launches in the USA\n\n".format(launch_data.shape[0]),
    tabulate(launch_data, headers="keys", tablefmt="fancy_grid"),
    sep="",
)
