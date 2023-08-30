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

rocket_launch_data["date"] = rocket_launch_data["date"].astype(str)
rocket_launch_data["time"] = rocket_launch_data["time"].astype(str)

print(tabulate(rocket_launch_data, headers='keys', tablefmt='fancy_grid'))

for i in rocket_launch_data.index:
    weather = get_weather(
        weather_url,
        rocket_launch_data["pad.latitude"][i],
        rocket_launch_data["pad.longitude"][i],
        (rocket_launch_data["date"][i]),
        (rocket_launch_data["time"][i]),
    )

    print(
        "\nWeather for {}:\n".format(rocket_launch_data.name[i]),
        tabulate(weather, headers="keys", tablefmt="fancy_grid"),
        sep="",
    )
