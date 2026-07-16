# Bulk file renamer
A command-line tool for bulk renaming files within a specified directory. It allows appending a custom prefix to file names and filtering target files by their extension.

## Features
* Renames all files in a target directory

* Adds a user-defined prefix to filenames

* Filters files by extension using the --ext argument

## Quickstart
Navigate to the project directory and execute the script via terminal.

#### Bash:
```
# Rename all files in a directory
python renamer.py path/to/directory PREFIX

# Rename only specific file types (like .jpg)
python renamer.py path/to/directory PREFIX --ext .jpg
```

#### Sample Output:
```
$ python py renamer.py test_files 2026-07-17 --ext jpg
Changed: 2026-07-16_photo.jpg -> 2026-07-17_2026-07-16_photo.jpg
```