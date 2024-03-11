from app import app
from models import Playlist, Song, PlaylistSong


def seed():
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    seed()