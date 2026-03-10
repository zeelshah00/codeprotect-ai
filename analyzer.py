import csv

#Load from CSV
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
        lines = code.split("\n")
        for line_number, line in enumerate(lines):
            for pattern in vuln:
                if pattern["pattern"] in line: 
                    finding = {
                        "title": pattern["title"],
                        "severity": pattern["severity"],
                        "line": line_number,
                        "explanation": pattern["explanation"]
                    }

                    findings.append(finding)
                      
        return findings

