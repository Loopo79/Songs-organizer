import mutagen
from pathlib import Path
import os
import shutil

songs_path = Path('songs/')
albums_path = Path('albums/')
list()

curr_album = ''
albums_dict: dict[str:list[Path]] = {}
for song_path in songs_path.iterdir():
    song = mutagen.File(song_path, easy=True)
    album:str = song['album']
    albums_dict.setdefault(album[0], list()).append(song_path)
    
songs_count = albums_count = 0

for album in albums_dict:
    while True:
        try:
            os.makedirs(albums_path/album, exist_ok=True)
            albums_count += 1
            break
        except:
            print("Invalid directory name:", album)
            album = input("Enter a valid album name: ")

    for song in albums_dict[album]:
        shutil.move(song, albums_path/album/song.name)
        songs_count += 1

print(f"\nCreated {albums_count} album folders with {songs_count} songs.")

