import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Bulk file renamer')
    parser.add_argument('catalog', help='Path to directory with files')
    parser.add_argument('prefix', help='Text to be added at the beginning of the filename')
    parser.add_argument('--ext', help='Change only files with following extention', default=None)

    args = parser.parse_args()

    # making sure target extension has a dot at the beginning if not mentioned
    target_ext = args.ext
    if target_ext and not target_ext.startswith('.'):
        target_ext = f'.{target_ext}'

    folder = Path(args.catalog)

    if not folder.exists() or not folder.is_dir():
        print('Error: Provided catalog does not exist or isn\'t a directory')
        return
    
    for element in folder.iterdir():
        if element.is_file(): # skipping subfolders
            # filtering by ext
            if target_ext and element.suffix != target_ext:
                continue # skipping

            new_name = f'{args.prefix}_{element.name}'
            new_path = folder / new_name

            element.rename(new_path)
            print(f'Changed: {element.name} -> {new_name}')

if __name__ == '__main__':
    main()