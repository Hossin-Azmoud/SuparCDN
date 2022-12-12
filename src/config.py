from json import loads, dump
from pathlib import Path

def loadConfig(path: Path):
    with open(str(path)) as fp:
        content = loads(fp.read())
        print(content)
        return content

def overWriteConfig(path: Path, data: dict):
    with open(str(path), "w+") as fp:
        dump(data, fp)
