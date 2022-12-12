# TODO GetUserAvatar(uuid: int) -> imgBytes           
# TODO GetUserBackground(uuid: int) -> imgBytes          
# TODO GetUserPostImgs(uuid: int, postId: int) -> imgBytes[]         
# TODO PostUserAvatar(Mime: img, uuid: int) -> result          
# TODO PostUserBackground(Mime: img, uuid: int) -> result
# TODO UpdateUserAvatar(uuid: int, NewMime: img) -> imgBytes         
# TODO UpdateUserBackground(uuid: int, NewMime: img) -> imgBytes             
# TODO PostUserPostImgs(Mimes: img[] | img, uuid, postId: int) -> result
# TOTAL TODOS: 8 (0/8). 
# TOTAL TODOS: 8 (0/8). 


from flask import Flask, request, send_file
from Funcs import makeResponse, SaveUserImage, getUserImage, SaveUserBackground, getUserBg
from json import loads

app = Flask(__name__)

# Done : not tested tho

@app.route("/Zimg/addAvatar", methods=["POST"]) # Not implemented!
def PostUserAvatar():
    data = request.json
    if "id" in data and "mime" in data:
        SaveUserImage(data)

    return makeResponse(400, "could not find id or mime in request form data! please recheck")



@app.route("/Zimg/<uuid>", methods=["GET"]) # Not implemented!
def GetUserAvatar(uuid):
    result = getUserImage(uuid)
    if result:
        file, ext = result
        return send_file(file, mimetype=f'image/{ext}')

    return makeResponse(500, "server could not find config file.")
    
@app.route("/Zimg/addbg", methods=["POST"]) # Not implemented!
def PostUserBackground():
    data = request.json
    if "id" in data and "mime" in data:
        SaveUserBackground(data)

    return makeResponse(400, "could not find id or mime in request form data! please recheck")




@app.route("/Zimg/bg/<uuid>", methods=["GET"]) # Not implemented!
def GetUserBackground(uuid):
    result = getUserBg(uuid)

    if result:
        file, ext = result
        return send_file(file, mimetype=f'image/{ext}')

    return makeResponse(500, "server could not find config file.")



@app.route("/Zimg/post/<uuid>/<postID>", methods=["GET"]) # Not implemented!
def GetUserPostImgs(uuid, postID):

    return f"Not implemented, but you have requested post ID: {postID} for UUID: {uuid}"



@app.route("/Zimg/", methods=[]) # Not implemented!
def UpdateUserAvatar():

    return "Not implemented"

@app.route("/Zimg/", methods=[]) # Not implemented!
def UpdateUserBackground():

    return "Not implemented"

@app.route("/Zimg/", methods=[]) # Not implemented!
def PostUserPostImgs():

    return "Not implemented"




if __name__ == '__main__':
    app.run(debug=True)


"""
PREVIOUS archi/APi
@app.route("/Zimg/get", methods=["GET"])
def GetUserAvatar():
   
    # Get an image or multiple images. 
    
    Data = request.values
    if "id" in Data and "type" in Data:
        id_ = Data["id"]
        type_ = Data["type"]       
        if "PostID" in Data:
            return GetPostImages(id_, Data["PostID"])
        else:
            pass
            
    return makeResponse(404, "Image could not be found.")

@app.route("/Zimg/add", methods=["POST"])
def PostImage():
    
    # Accepts: id_ - required, type - POST|IMG|BG, postId (Only if type === POST)
 
    data = request.json
    if "id" in data and "type" in data:
        if not "content" in data:
            return makeResponse(404, "request with no content")
        id_ = request.values["id"]
        type_ = request.values["type"]       
        content_ = loads(request.values["content"])
        
        if type_ == IType.POST:
            
    return makeResponse(404, "Image could not be added as id and type are messig.")


@app.route("/Zimg/update", methods=["POST"])
def update():
    data = request.json
    assert False, "Not implemented!"

@app.route("/Zimg/Del", methods=["POST"])
def delete():
    data = request.json
    assert False, "Not implemented!"

"""
