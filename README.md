# zip-app

A python script zips each folder in the current directory to their respective `<FOLDER-NAME>.zip`. Each folder will only zip files that match the given pattern `-p`

### Prerequisites
```
Python
```

### Usage

```
usage: zip-app.py [-h] [-p PATTERN]

options:
  -h, --help            show this help message and exit
  -p PATTERN, --pattern PATTERN
                        pattern
```

1) Move the zip-app.py to the directory with folders you wish to zip
2) Open command line terminial to the current directory with the python script
3) Use this command in the terminal (change python3 to your current python version) and give a pattern `-p` that matches files you wish to zip
```
  python3 zip-app.py -p "*"
```
#### Pattern Examples
- `-p "*"` zips all files in the folder
- `-p ".txt"` will zip all files that have .txt in their name 
