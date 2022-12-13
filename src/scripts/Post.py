
from requests import post
from base64 import b64encode

api = "http://localhost:8500"

# Endpoints.
addIMG = f"{api}/Zimg/addAvatar"
addBG = f"{api}/Zimg/addbg"
addPOST = f"{api}/Zimg/NewPostImg"

def MakeMime(fp):
    ext = fp.name.split("/")[-1].split(".")[1]
    print(ext)
    enc = b64encode(fp.read()).decode()
    return f"data:image/{ext};base64,{enc}"

def addAvatar(uuid: int | str, Mime: str) -> dict:
    
    res = post(addIMG, json={
        "id": uuid,
        "mime": Mime
    })

    return res.json()

def addbg(uuid: int | str, Mime: str) -> dict:
    res = post(addBG, json={
        "id": uuid,
        "mime": Mime
    })

    return res.json()

def addPost(uuid, Mime, postid=1):
    res = post(addPOST, json={
        "id": uuid,
        "mime": Mime,
        "postID": postid
    })

    return res.json()


def main():
    path = "./img/img.png"

    with open(path, "rb") as fp:
        print("Opening..")
        uuid = 1
        print("Converting..")
        mime = MakeMime(fp)
        print("Sending..")
        res = addAvatar(uuid, mime)
        print(res)
        res = addbg(uuid, mime)
        print(res)
        
if __name__ == "__main__":
    main()



