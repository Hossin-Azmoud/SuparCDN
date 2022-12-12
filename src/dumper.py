from pathlib import Path
from base64 import b64decode
from CDN import cdn
from Enums import IType
from json import dump
from loaders import Load_Config

assert cdn, "CDN not found in env! consider adding a path with set cdn={YOUR_CDN_PATH.}"

def writeConfig(path: str, data: dict):
    with open(path, "w+") as fp: return dump(data, fp)

def GetData(IMime, TypeIndex: int) -> tuple:
    """ 
        gets the image ext and bytes. 
        data:image/{ext};base64,{encoded data}
    """

    Extention = IMime.split(";")[0].split(":")[1].split("/")[1]
    Bytes = b64decode(IMime.split(";")[1].split(",")[1].encode())
    FileName = IType.NAMES[TypeIndex]
    return Bytes, f"{FileName}.{Extention}", Extention

def addImg(uuid: int | str, T: int, IMime):
    new = False
    if isinstance(T, str): T = int(T)
    
    UPath = Path(cdn, str(uuid))
    
    if not UPath.exists:
        UPath.mkdir()
        new = True

    if new:
        configFile = (UPath / "Config.json")

        if not configFile.exists():
            bytes_, name, ext = GetData(IMime, T)
            writeConfig(configFile, {
                "ext": ext
            })

            if not isinstance(bytes_, bytes): bytes_ = bytes_.encode()

            with open(str(UPath / name), "wb+") as Ip: Ip.write(bytes_)

            return makeResponse(200, "The image was added!")

    return "ALready exists."

def addPostImages(uuid, postid, IMimes):
    
    UPosts_Path = Path(cdn, str(uuid), "Posts")
    
    if not UPosts_Path.exists:
        UPosts_Path.mkdir()
        new = True

    configFile = (UPosts_Path / "Config.json")

    if configFile.exists():
        config = Load_Config(configFile)

        bytes_, name, ext = GetData(IMime, T)
        
        writeConfig(configFile, {
            "ext": ext
        })

        if not isinstance(bytes_, bytes): bytes_ = bytes_.encode()

        with open(str(UPath / name), "wb+") as Ip: Ip.write(bytes_)

        return makeResponse(200, "The image was added!")

    
    
