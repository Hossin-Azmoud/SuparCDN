from flask import Flask, request
from Enums import IType
from json import loads
from dataclasses import dataclass
app = Flask(__name__)

"""
    IMG: 0
    BG: 1
"""



@dataclass
class Response:
    code: int
    data: any

    def __dict__(self) -> dict:
        return {
            "code": self.code,
            "data": self.data
        }

    def Json(self) -> str:
        return dumps(self.__dict__)
    
def makeResponse(code: int = 200, data: any = "No data") -> None: return dict(Response(code, data))

def GetPostImages(uuid: int | str, post_id int | str) -> bytes:
    """ get every image in this path: {cdn}/{uuid}/Posts/{post_id}/*.* """
    pass

def GetImg(uuid: int | str, T: int):
    
    if isinstance(T, str): T = int(T)
    # [ Get the image from {cdn}/{uuid}/{IType.STR[T]}.ext ]
    pass

def addImg(uuid: int | str, T: int):
    if isinstance(T, str): T = int(T)
    # TODO Get the extention from mime.
    """
    
    """
    # TODO Get the bytes from the mime.
    # TODO Dump the info to a file ({Ext: *}).
    # TODO Dump the img to its proper place {cdn}/{uuid}/{IType.STR[T]}.ext 
    

@app.route("/Zimg/get", methods=["GET"])
def GetImage():
    """
    Get an image or multiple images. 
    """
    Data = request.values
    if "id" in Data and "type" in Data:
        id_ = Data["id"]
        type_ = Data["type"]       
        if "PostID" in Data:
            return GetPostImages(id_, Data["PostID"])
        else:
            
        
    return makeResponse(404, "Image could not be found.")

@app.route("/Zimg/add", methods=["POST"])
def PostImage():
    """
        Accepts: id_ - required, type - POST|IMG|BG, postId (Only if type === POST)
    """
    
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


if __name__ == '__main__':
    app.run(debug=True)
