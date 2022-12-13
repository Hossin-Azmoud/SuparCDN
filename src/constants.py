
from os import environ

if "cdn" in environ:
    CDN = environ["cdn"]    
else:
    CDN = ""

API_URL = "http://localhost:8500"
