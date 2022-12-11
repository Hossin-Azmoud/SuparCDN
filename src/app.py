from flask import Flask, request

app = Flask(__name__)


@app.route("/Zimg/get", methods=["GET"])
def GetImage():

    if "id" in request.values:
        id_ = request.values["id"]
        return f"<h1 style=\"font-size:30px;font-family: helvetica;font-weight:300;\"> Hello, world! {id_}</h1>"
    return "Image was not provided."


@app.route("/Zimg/add", methods=["POST"])
def PostImage():
    """
        Accepts: id - required, img - required if bg is not present, bg required if img is not present.
    """
    data = request.json
    
    assert False, "Not implemented!"

       

@app.route("/Zimg/update", methods=["POST"])
def update():
    data = request.json
    assert False, "Not implemented!"



if __name__ == '__main__':
    app.run(debug=True)
