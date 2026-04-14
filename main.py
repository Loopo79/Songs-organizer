import mutagen
from pathlib import Path

songs_path = Path('songs/')
albums_path = Path('songs/')
list()

curr_album = ''
albums_dict: dict[str:list[Path]] = {}
for song_path in songs_path.iterdir():
    song = mutagen.File(song_path, easy=True)
    album:str = song['album']
    albums_dict.setdefault(album[0], list()).append(song_path)
    
print(albums_dict)



