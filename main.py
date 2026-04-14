import mutagen
from pathlib import Path
import os
import shutil
import re

songs_dir = Path('songs/')
albums_dir = Path('albums/')


def is_valid_folder_name(folder_name: str) -> bool:
    return not re.search('[/\0]', folder_name)

tracks_by_album: dict[str, list[Path]] = {}
for song_path in songs_dir.iterdir():
    try:
        # mutagen.File(song_path, easy=True)['album'] returns ['album_name']
        album_name:str = mutagen.File(song_path, easy=True)['album'][0]

    except:
        print(f"Error: the file {song_path} is either not a audio file or does not have the album tag.")
        print(f"Skipping {song_path}")
        continue
        
    tracks_by_album.setdefault(album_name, list()).append(song_path)
    

songs_count = albums_count = 0
for album_key in tracks_by_album:
    album_name = album_key
    while True:
        if is_valid_folder_name(album_name):
            os.makedirs(albums_dir/album_name, exist_ok=True)
            print("Created directory:", albums_dir/album_name)
            albums_count += 1
            break

        else:
            print("Error: Invalid directory name:", album_name)
            album_name = input("Enter a valid album name: ")

    for song in tracks_by_album[album_key]:
        shutil.move(song, albums_dir/album_name/song.name)
        songs_count += 1

print(f"\nCreated {albums_count} album folders with {songs_count} songs.")

