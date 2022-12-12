from json import load, dump

def loadConfig(path: Path):
    with open(str(path), "w+") as fp:
        return load(fp)

def overWriteConfig(path: Path, data: dict):
    with open(str(path), "w+") as fp:
        dump(data, fp)
