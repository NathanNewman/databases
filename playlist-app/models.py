"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = "playlists"

    def __repr__(self):
        p = self
        return f"<Playlist {p.id}: {p.name} Description: {p.description}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    songs = db.relationship(
        'PlaylistSong', backref='playlist', cascade='all, delete-orphan')

    @classmethod
    def add_playlist(cls, form):
        name = form.name.data
        description = form.description.data
        return cls(name=name, description=description)


class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    def __repr__(self):
        s = self
        return f"<Song {s.id}: {s.title} Artist: {s.artist}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    playlists = db.relationship(
        'PlaylistSong', backref='song', cascade='all, delete-orphan')

    @classmethod
    def add_song(cls, form):
        title = form.title.data
        artist = form.artist.data
        return cls(title=title, artist=artist)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlist_songs"

    def __repr__(self):
        ps = self
        return f"<Playlist: {ps.playlist_id} Song: {ps.song_id}>"

    playlist_id = db.Column(db.Integer, db.ForeignKey(
        'playlists.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey(
        'songs.id'), primary_key=True)

    @classmethod
    def add_song(cls, playlist_id, form):
        song_id = form.song.data
        return cls(playlist_id=playlist_id, song_id=song_id)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
