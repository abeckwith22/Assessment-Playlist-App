"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    
    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key = True, auto_increment = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = True)

    # ADD THE NECESSARY CODE HERE


class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key = True, auto_increment = True)
    title = db.Column(db.String(100), nullable = False)
    artist = db.Column(db.String(100), nullable = False)

    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlists_songs"

    id = db.Column(db.Integer, primary_key = True, auto_increment = True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))

    def __repr__(self):
        return f"< playlist_id={self.playlist_id} song_id={self.song_id} >"

    # ADD THE NECESSARY CODE HERE


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""
    app.app_context().push()

    db.app = app
    db.init_app(app)
