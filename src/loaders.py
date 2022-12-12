from os import environ
from json import load
assert environ["cdn"], "CDN env var not found!"
CDN = environ["cdn"]


def Load_Config(path):
    with open(path, "r") as fp:
        return load(fp)
