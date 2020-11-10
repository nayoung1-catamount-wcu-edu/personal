library(rjson)

sh0 <- fromJSON(file = "D:/SpotifyData/my_spotify_data/StreamingHistory0.json")
sh1 <- fromJSON(file = "D:/SPotifyData/my_spotify_data/StreamingHistory1.json")

streaming_history <- rbind(sh0, sh1)
head(streaming_history, n=5)