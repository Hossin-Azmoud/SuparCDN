from os import environ

assert environ["cdn"], "CDN env var not found!"

def loadImage(id_: int) -> bytes:
    pass

