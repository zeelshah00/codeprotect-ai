import csv


# Load from CSV
def load_vulnerabilities():
    vuln = []

    with open("vulnerabilities.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            vuln.append(row)

    return vuln


def analyze_code(code):
    vuln = load_vulnerabilities()
    findings = []
    risk = "Safe"
    lines = code.split("\n")
    for line_number, line in enumerate(lines, start=1):
        for pattern in vuln:
            if pattern["pattern"] in line:
                finding = {
                    "pattern": pattern["pattern"],
                    "category": pattern["category"],
                    "title": pattern["title"],
                    "severity": pattern["severity"],
                    "line": line_number,
                    "explanation": pattern["explanation"],
                    "snippet": line,
                }

                findings.append(finding)
    
    for finding in findings:

        if finding["severity"] == "High":
            risk = "High"
            break

        elif finding["severity"] == "Medium" and risk != "High":
            risk = "Medium"

        elif finding["severity"] == "Low" and risk == "Safe":
            risk = "Low"
                   
    return findings, risk
