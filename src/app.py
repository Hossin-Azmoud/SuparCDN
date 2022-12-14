from flask import Flask, request, send_file

from Funcs import (
    makeResponse, 
    SaveUserImage, 
    getUserImage, 
    SaveUserBackground, 
    getUserBg, 
    saveUserPostImage,
    GetUserPostImg
)

from json import loads

app = Flask(__name__)
PORT = 8500

#--------------------------------------------------------------DONEe------------------------------------------------------------------------
@app.route("/Zimg/addAvatar", methods=["POST"])
def PostUserAvatar():
    data = request.json
    if "id" in data and "mime" in data:
        result = SaveUserImage(data)
        return result

    return makeResponse(400, "could not find id or mime in request form data! please recheck")
@app.route("/Zimg/<uuid>/<fname>", methods=["GET"])
def GetUserAvatar(uuid, fname):
    result = getUserImage(uuid, fname)
    if result:
        file, ext = result
        return send_file(file, mimetype=f'image/{ext}')

    return makeResponse(500, "server could not find config file.")   
@app.route("/Zimg/addbg", methods=["POST"])
def PostUserBackground():
    data = request.json
    if "id" in data and "mime" in data:
        result = SaveUserBackground(data)
        print(result)
        return result

    return makeResponse(400, "could not find id or mime in request form data! please recheck")
@app.route("/Zimg/bg/<uuid>/<fname>", methods=["GET"])
def GetUserBackground(uuid, fname):
    result = getUserBg(uuid, fname)

    if result:
        file, ext = result
        return send_file(file, mimetype=f'image/{ext}')

    return makeResponse(500, "server could not find config file.")
@app.route("/Zimg/NewPostImg", methods=["POST"])
def PostUserPostImgs():
    data = request.json

    if "id" in data and "mime" in data and "postID" in data:
        result = saveUserPostImage(data)
        return result

    return makeResponse(400, "could not find id or mime in request form data! please recheck")
@app.route("/Zimg/post/<uuid>/<postID>/<fname>", methods=["GET"])
def GetUserPostImgs(uuid, postID, fname):
    result = GetUserPostImg(uuid, postID, fname)
    if result:
        file, ext = result
        return send_file(file, mimetype=f'image/{ext}')

    return makeResponse(500, "server could not find config file.")
#--------------------------------------------------------------DONEe------------------------------------------------------------------------



@app.route("/Zimg/", methods=["POST"]) # Not implemented!
def UpdateUserAvatar(): return "Not implemented"

@app.route("/Zimg/", methods=["POST"]) # Not implemented!
def UpdateUserBackground(): return "Not implemented"


if __name__ == '__main__':
    app.run(port=PORT, debug=True)
