import mutagen
from pathlib import Path
import os
import shutil

songs_dir = Path('songs/')
albums_dir = Path('albums/')

tracks_by_album: dict[str, list[Path]] = {}
for song_path in songs_dir.iterdir():
    # mutagen.File(song_path, easy=True)['album'] returns ['album_name']
    album_name:str = mutagen.File(song_path, easy=True)['album'][0]
    
    tracks_by_album.setdefault(album_name, list()).append(song_path)
    

songs_count = albums_count = 0
for album_name in tracks_by_album:
    valid_album_name = album_name
    while True:
        try:
            os.makedirs(albums_dir/valid_album_name, exist_ok=True)
            print("Created directory:", albums_dir/valid_album_name)
            albums_count += 1
            break

        except:
            print("Invalid directory name:", valid_album_name)
            valid_album_name = input("Enter a valid album name: ")

    for song in tracks_by_album[album_name]:
        shutil.move(song, albums_dir/valid_album_name/song.name)
        songs_count += 1

print(f"\nCreated {albums_count} album folders with {songs_count} songs.")

