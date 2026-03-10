from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.form.get("code", "")
    language = request.form.get("language", "python")

    findings = []

    return render_template(
        "results.html", code=code, language=language, findings=findings
    )


if __name__ == "__main__":
    app.run(debug=True)
