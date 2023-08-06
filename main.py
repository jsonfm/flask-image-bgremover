from flask import Flask, render_template, jsonify, request
from utils.background import remove_bg_image


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/removebg", methods=["POST"])
def remove_bg():
    image = request.json.get("image")
    if image is not None:
        result = remove_bg_image(
            image, 
            to_base64=True, 
            myme=True,
            _format="png"
        )
        response = {
            "result": result
        }
        return response
    return "Something went wrong!"
