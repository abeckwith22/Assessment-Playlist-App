from flask import Flask, redirect, render_template
# from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")

##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    playlist_songs = PlaylistSong.query.filter_by(playlist_id=playlist_id).all() # getting the song_ids from the playlist_id query to playlists_songs db
    songs = []
    for row in playlist_songs:
        songs.append(Song.query.filter_by(id=row.song_id).first())

    playlist = Playlist.query.filter_by(id=playlist_id).first()
    return render_template("playlist.html", playlist=playlist, songs=songs)

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - [x] if form not filled out or invalid: show form
    - [x] if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form = PlaylistForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data

        new_playlist = Playlist(name=name, description=description)
        db.session.add(new_playlist)
        db.session.commit()
        return redirect('/playlists')
    
    return render_template('new_playlist.html', form=form)


    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""    
    """Show detail on specific playlist."""
    playlist_songs = PlaylistSong.query.filter_by(song_id=song_id).all()
    playlists = []
    for row in playlist_songs:
        playlists.append(Playlist.query.filter_by(id=row.playlist_id).first())

    song = Song.query.filter_by(id=song_id).first()
    return render_template("song.html", song=song, playlists=playlists)
    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    form = SongForm()
    if form.validate_on_submit():
        title = form.title.data
        artist = form.artist.data

        new_song = Song(title=title, artist=artist)
        

        db.session.add(new_song)
        db.session.commit()

        return redirect('/songs')
    
    return render_template('new_song.html', form=form)

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist
    curr_on_playlist = PlaylistSong.query.filter_by(playlist_id=playlist_id).all()
    curr_on_playlist_ids = []
    for row in curr_on_playlist:
        curr_on_playlist_ids.append(row.song_id)
    song_choices = Song.query.all()

    print("-"*50)
    print("Playlist Name: ", playlist.name)
    print("Playlist Description: ", playlist.description)
    print("Song objs in Playlist: ", curr_on_playlist)
    print("Song_ids in Playlist: ", curr_on_playlist_ids)
    print("Song_ids in DB: ", song_choices)
    print("-"*50)

    form.song.choices = []

    for song in song_choices:
        if not (song.id in curr_on_playlist_ids):
            form.song.choices.append(song.id)

    # form.song.choices = [song_id for song_id in curr_on_playlist if song_id not in curr_on_playlist]
    # form.song.choices = [id for id in curr_on_playlist.song_id]

    if form.validate_on_submit():
        # add song_id and playlist_id to PlaylistSong and I think that's it...
        song = form.song.data # would show the songs id

        relationship = PlaylistSong(song_id=song, playlist_id=playlist_id)
        db.session.add(relationship)
        db.session.commit()
        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html", playlist=playlist, form=form)
