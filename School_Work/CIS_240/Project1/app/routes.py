from flask import render_template, redirect, url_for, request
from app import app
from album import Album

albums = []

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    newAlbumID = request.form.get("albumID", "")
    newAlbumName = request.form.get("albumName", "")
    newAlbumType = request.form.get("albumType", "")
    newAlbumReleaseDate = request.form.get("albumReleaseDate", "")

    newAlbum = Album(albumID=newAlbumID, albumName=newAlbumName, albumType=newAlbumType, albumReleaseDate=newAlbumReleaseDate)
    albums.append(newAlbum)
    return redirect(url_for("index"))
  return render_template("index.html", pageheader="All Albums", albums=albums)