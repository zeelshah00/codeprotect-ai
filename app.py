from flask import Flask, render_template, request
from analyzer import analyze_code
from history import historical_data

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.form.get("code", "")
    language = request.form.get("language", "python")

    findings = analyze_code(code)
    historical_data(code, findings, language)

    return render_template(
        "results.html", code=code, language=language, findings=findings)

@app.route("/history", methods=["GET"])
def history(): ##additional logic and inputs needed here to give to history.html so that it can process the page
    return render_template("history.html")

    


if __name__ == "__main__":
    app.run(debug=True)
