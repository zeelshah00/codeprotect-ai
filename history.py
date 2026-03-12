import sqlite3

def historical_data(code, findings, language):
    db = sqlite3.connect("scans.db")
    cursor = db.cursor()

    # Insert Scan
    cursor.execute("INSERT INTO scans (language, code) VALUES (?, ?)", (language, code))
    scan_id = cursor.lastrowid

    # Insert findings
    for finding in findings:
        cursor.execute(
            "INSERT INTO findings (scan_id, title, severity, line, explanation) VALUES (?, ?, ?, ?, ?)",
            (
                scan_id,
                finding["title"],
                finding["severity"],
                finding["line"],
                finding["explanation"],
            ),
        )

    db.commit()
    db.close()
    return None