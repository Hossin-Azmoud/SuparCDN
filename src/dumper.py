from os import environ, Path, path

assert environ["cdn"], "CDN env var not found!"
CDN = environ["cdn"]

def dumpImage(ImgMEMO: str, uuid: int | str, imageType: str) -> int:
    # /cdn/<Uid>/img
    
    path = Path(path.join(CDN, str(uuid)))
    pass

