import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

sh0 = pd.read_json("D:/SpotifyData/my_spotify_data/StreamingHistory0.json")
sh1 = pd.read_json("D:/SpotifyData/my_spotify_data/StreamingHistory1.json")

streaming_history = sh0.append(sh1)

artist_group = streaming_history.groupby("artistName")["msPlayed"].sum()

artist_group = artist_group.sort_values(ascending=False)
artist_group = pd.DataFrame(artist_group)

n = int(input("How many artists to you want to see? "))

plt1 = (1, 1, 1)
plt1 = px.bar(artist_group.nlargest(n, "msPlayed"), title="Top {} Artists by msPlayed".format(n))

#plt2 = (1, 1, 2)
#plt2 = px.bar(artist_group.nlargest(n, "msPlayed"), title="Top {} Tracks by msPlayed".format(n))

print(plt1.show())