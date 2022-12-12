
from models import Response
from base64 import b64decode
from pathlib import Path
from CDN import CDN
from json import load, dump
from config import loadConfig, overWriteConfig 
assert CDN, "Could not find the cdn, check if it is assigned in the env vars."

TYPES = [
    "img", "bg"
]

IMG = 0
BG = 1

def makeResponse(code: int = 200, data: any = "No data") -> None: return Response(code, data).make()

def Unpack(IMime, TypeIndex: int) -> tuple:
    """ Unpacking the mime image. """

    Extention = IMime.split(";")[0].split(":")[1].split("/")[1]
    Bytes = b64decode(IMime.split(";")[1].split(",")[1].encode())
    FileName = TYPES[TypeIndex]
    return Bytes, f"{FileName}.{Extention}"

def SaveUserImage(data: dict, update = False) -> Response:

    MIME, ID = data["mime"], data["id"] 
    if isinstance(ID, int): ID = str(ID)
    Upath = Path(CDN) / ID
    ConfigPath = Path(CDN) / ID / "config.json"

    if not Upath.exists(): Upath.mkdir()

    if ConfigPath.exists() and not update:
        Config = loadConfig(ConfigPath)
    
        if "img" in Config:
            return makeResponse(400, "Image already exists!")    

    Bytes, FName = Unpack(MIME, IMG)
    Config["img"] = FName
    ImagePath = Upath / FName
    with open(ImagePath, "w+") as fp: 
        fp.write(Bytes)

    overWriteConfig(ConfigPath, Config)

    return makeResponse(200, "Success.")

def getUserImage(uuid: int | str) -> tuple[str, str] | bool:
    UFolder = Path(CDN) / str(uuid)
    ConfigPath = UFolder / "config.json"

    if ConfigPath.exists():
        conf = loadConfig(ConfigPath)
        print(conf)
        Extention = conf["img"].split(".")[1] # get img ext.
        FilePath = UFolder / conf["img"]
        if FilePath.exists():
            return FilePath, Extention

    return False

def SaveUserBackground(data: dict) -> None:
    MIME, ID = data["mime"], data["id"] 
    if isinstance(ID, int): ID = str(ID)
    Upath = Path(CDN) / ID
    ConfigPath = Path(CDN) / ID / "config.json"

    if not Upath.exists(): Upath.mkdir()

    if ConfigPath.exists() and not update:
        Config = loadConfig(ConfigPath)
    
        if "bg" in Config:
            return makeResponse(400, "Image already exists!")    

    Bytes, FName = Unpack(MIME, BG)
    Config["bg"] = FName
    ImagePath = Upath / FName

    with open(ImagePath, "w+") as fp:
        fp.write(Bytes)

    overWriteConfig(ConfigPath, Config)

    return makeResponse(200, "Success.")


def getUserBg(uuid: str | int) -> tuple[str, str] | bool:
    UFolder = Path(CDN) / str(uuid)
    ConfigPath = UFolder / "config.json"
   
    if ConfigPath.exists():
        conf = loadConfig(ConfigPath)

        Extention = conf["bg"].split(".")[1] # get img ext.
        FilePath = UFolder / conf["bg"]
        if FilePath.exists():
            return FilePath, Extention

    return False