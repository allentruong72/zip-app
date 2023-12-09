from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path
import argparse

p = Path('./')

argParser = argparse.ArgumentParser()
argParser.add_argument("-p", "--pattern", help="pattern")

args = argParser.parse_args()

for dir in p.iterdir():
    if Path.is_dir(dir):
        zip_path = './' + dir.name + '.zip'
        dir_to_zip = dir
        folder = Path(dir_to_zip)

        with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zip:
            for file in folder.rglob(args.pattern):
                if not Path.is_dir(file):
                    zip.write(file, arcname=file.name)