import mutagen
from pathlib import Path
import os
import shutil
import re

def is_valid_folder_name(folder_name: str) -> bool:
    return not re.search('[/\0]', folder_name)

def organize_songs(songs_dir: Path = Path("./songs/")):
    """
    Gets a Path, songs_dir which has audio files
    Returns a dict
    {
        album_name: [song_path, ...]
    }
    """
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
    return tracks_by_album
    
def move_into_folders(files_by_album, folders_dir: Path = Path("./albums/")) -> tuple[int, int]:
    """
    Gets a dict
    {
        folder_name: [file_path, ...]
    }
    And a Path, folders_dict to store the folders in
    Moves the files into the corresponding folders
    Returns (folders_count, files_count)
    """
    files_count = folders_count = 0
    for file_key in files_by_album:
        file_name = file_key
        while True:
            if is_valid_folder_name(file_name):
                os.makedirs(folders_dir/file_name, exist_ok=True)
                print("Created directory:", folders_dir/file_name)
                albums_count += 1
                break

            else:
                print("Error: Invalid directory name:", file_name)
                file_name = input("Enter a valid album name: ")

        for file in files_by_album[file_key]:
            shutil.move(file, folders_dir/file_name/file.name)
            songs_count += 1
    return folders_count, files_count

if __name__ == "__main__":
    songs_dir = Path('./songs/')
    albums_dir = Path('./albums/')

    tracks_by_album = organize_songs(songs_dir)

    albums_count, songs_count = move_into_folders(tracks_by_album, albums_dir)

    print(f"\nCreated {albums_count} album folders with {songs_count} songs.")

