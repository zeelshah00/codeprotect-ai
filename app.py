from flask import Flask, render_template, request
import math
from analyzer import analyze_code
from history import historical_data
from prompts import ai_suggestions
import sqlite3

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.form.get("code", "")
    language = request.form.get("language", "python")

    findings, risk = analyze_code(code)
    len_findings = len(findings)
    historical_data(code, findings, language)

    if findings: 
        suggestion = ai_suggestions(code, findings, language)
    else:
        suggestion = "AI explanation unavailable."

    return render_template(
        "results.html",
        code=code,
        language=language,
        findings=findings,
        len_findings=len_findings,
        risk=risk, 
        suggestion=suggestion
    )


@app.route("/history", methods=["GET"])
def history():
    page = request.args.get("page", 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page

    db = sqlite3.connect("scans.db")
    cursor = db.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM scans JOIN findings ON scans.id = findings.scan_id"
    )
    total_rows = cursor.fetchone()[0]

    cursor.execute(
        "SELECT * FROM scans JOIN findings ON scans.id = findings.scan_id ORDER BY created_at DESC LIMIT ? OFFSET ?",
        (per_page, offset),
    )

    history = cursor.fetchall()
    db.close()

    total_pages = math.ceil(total_rows / per_page)

    return render_template(
        "history.html", history=history, page=page, total_pages=total_pages
    )


if __name__ == "__main__":
    app.run(debug=True)
