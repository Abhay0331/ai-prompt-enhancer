from flask import Flask, render_template, request
from prompt_engine import enhance_prompt

app = Flask(__name__)

styles = [
    "Fantasy",
    "Cyberpunk",
    "Anime",
    "Realistic",
    "Mythological",
    "Dark Fantasy",
    "Cinematic",
    "Pixar",
    "Comic"
]


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        prompt = request.form["prompt"]
        style = request.form["style"]

        result = enhance_prompt(
            prompt,
            style
        )

    return render_template(
        "index.html",
        result=result,
        styles=styles
    )


if __name__ == "__main__":
    app.run(debug=True)