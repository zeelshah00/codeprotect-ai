
import sqlite3




def historical_data(code, findings, language):
    db = sqlite3.connect('scans.db')
    cursor = db.cursor()
    
    #Insert Scan
    cursor.execute("INSERT INTO scans (language, code) VALUES (?, ?)", (language, code))
    scan_id = cursor.lastrowid

    #Insert findings
    for finding in findings:
        cursor.execute("INSERT INTO findings (scan_id, title, severity, line, explanation) VALUES (?, ?, ?, ?, ?)", (scan_id, finding["title"], finding["severity"], finding["line"], finding["explanation"]))
    
    db.commit()
    db.close()
    return None

def get_history():

    db = sqlite3.connect("scans.db")
    cursor = db.cursor()

    history = cursor.execute(
        "SELECT * FROM scans JOIN findings ON scans.id = findings.scan_id ORDER BY created_at DESC"
    ).fetchall()

    db.close()

    return history