from app import app
from flask import request, jsonify

expenses = []

@app.route("/add", methods=["POST"])
def add_expense():
    data = request.get_json()
    expenses.append(data)
    return jsonify({"message": "Expense added"}), 201

@app.route("/summary", methods=["GET"])
def summary():
    return jsonify(expenses)

@app.route("/health")
def health():
    return "OK", 200
