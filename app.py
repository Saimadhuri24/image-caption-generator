from flask import Flask, render_template, request
import os

from predict import generate_caption

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    if "image" not in request.files:

        return "No image uploaded"

    image = request.files["image"]

    image_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        image.filename
    )

    image.save(image_path)

    caption = generate_caption(
        image_path
    )

    return render_template(
    "result.html",
    image_path=image_path,
    caption=caption
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)