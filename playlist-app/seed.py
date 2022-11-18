from app import app
from models import db, Playlist, Song, PlaylistSong

db.drop_all()
db.create_all()

PlaylistSong.query.delete()
Playlist.query.delete()
Song.query.delete()

pop = Playlist(
    name='Pop',
    description='Pop music playlist'
)

rap = Playlist(
    name='Rap',
    description='Rap music playlist'
)

rock = Playlist(
    name='Rock',
    description='Rock music playlist'
)

blank_space = Song(
    title='Anti-Hero',
    artist='Taylor Swift'
)

dark_horse = Song(
    title='Dark Horse',
    artist='Katty Perry'
)

soldier = Song(
    title='Soldier',
    artist='Eminem'
)

best_friend = Song(
    title='Best Friend',
    artist='Yelawolf'
)

thunderstruck = Song(
    title='Thunderstruck',
    artist='ACDC'
)

blank = PlaylistSong(
    playlist_id=1,
    song_id=1
)

dark = PlaylistSong(
    playlist_id=1,
    song_id=2
)

sol = PlaylistSong(
    playlist_id=2,
    song_id=3
)

best1 = PlaylistSong(
    playlist_id=2,
    song_id=4
)

best2 = PlaylistSong(
    playlist_id=3,
    song_id=4
)

thunder = PlaylistSong(
    playlist_id=3,
    song_id=5
)

db.session.add(pop)
db.session.add(rap)
db.session.add(rock)
db.session.add(blank_space)
db.session.add(dark_horse)
db.session.add(soldier)
db.session.add(best_friend)
db.session.add(thunderstruck)
db.session.add(blank)
db.session.add(dark)
db.session.add(sol)
db.session.add(best1)
db.session.add(best2)
db.session.add(thunder)

db.session.commit()
