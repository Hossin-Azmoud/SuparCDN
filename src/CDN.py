from os import environ

if "cdn" in environ:
    CDN = environ["cdn"]    
else:
    CDN = ""
