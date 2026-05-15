from datetime import datetime
import sqlite3
from flask import Flask, jsonify, request, render_template, g

DATABASE = "citypulse.db"
app = Flask(__name__)

def get_db():
    db = getattr(g, "db", None)
    if db is None:
        db = g.db = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        db.execute("""
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL,
                status TEXT NOT NULL DEFAULT 'new',
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)
        db.commit()

@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, "db", None)
    if db is not None:
        db.close()

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

# ======= Pages =======
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/map")
def map_page():
    return render_template("map.html")

# ======= API =======
@app.route("/api/report", methods=["POST"])
def create_report():
    data = request.get_json(force=True)
    description = data.get("description")
    latitude = data.get("latitude")
    longitude = data.get("longitude")

    if not description or latitude is None or longitude is None:
        return jsonify({"success": False, "error": "Missing required fields."}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO reports (description, latitude, longitude) VALUES (?, ?, ?)",
        (description, latitude, longitude),
    )
    db.commit()
    return jsonify({"success": True, "report_id": cursor.lastrowid})

@app.route("/api/reports")
def list_reports():
    db = get_db()
    cursor = db.execute("SELECT * FROM reports ORDER BY created_at DESC")
    reports = [dict(row) for row in cursor.fetchall()]
    return jsonify(reports)

@app.route("/api/report/<int:id>/status", methods=["PUT", "OPTIONS"])
def update_status(id):
    data = request.get_json(force=True)
    new_status = data.get("status")

    if new_status not in ("new", "progress", "done"):
        return jsonify({"success": False, "error": "Invalid status"}), 400

    db = get_db()
    db.execute("UPDATE reports SET status = ? WHERE id = ?", (new_status, id))
    db.commit()
    return jsonify({"success": True})

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)