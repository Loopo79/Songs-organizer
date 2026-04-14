# Songs-organizer
Organizes songs into folders based on their album names using metadata. 

---

## Workings
    1) iterates over each file in `songs_dir` and checks validity of file.
    2) Extracts the album metadata and creates a dictionary of `{album_name: [song1, song2, ...]}`
    3) Validates album names and creates corresponding folders.
    4) Moves songs into their respective album folders.

---

## Features
    - Automatically organizes songs into album based folders
    - Extracts album names from audio metadata
    - Dynamically handles invalid album names

---

## TODO
    1) Add windows support
    2) Add support for the option to map illegal characters to safe characters for folder names
    3) Convert into a CLI tool
