from flask import Flask, render_template, request
from analyzer import analyze_code
from history import historical_data, get_history

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.form.get("code", "")
    language = request.form.get("language", "python")

    findings,risk = analyze_code(code)
    len_findings = len(findings)
    historical_data(code, findings, language)

    return render_template(
        "results.html", code=code, language=language, findings=findings, len_findings=len_findings, risk=risk)

@app.route("/history", methods=["GET"])
def history():
    history = get_history()
    print(history)
    return render_template("history.html", history=history)

    


if __name__ == "__main__":
    app.run(debug=True)
