albums = []

class Album:
  def __init__(self, albumID, albumName, albumType , albumReleaseDate):
    self.albumID = albumID
    self.albumName = albumName
    self.albumType = albumType
    self.albumReleaseDate = albumReleaseDate
    albums.append(self)