"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("Playlist Name:", validators=[InputRequired(message="Please enter a name for your playlist")])
    description = TextAreaField("Playlist Description:", validators=[InputRequired(message="Please enter a name for your playlist")])

    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField("Title:", validators=[InputRequired(message="Please enter a Song Title")])
    artist = StringField("Artist:", validators=[InputRequired(message="Please enter an artist")])

    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
