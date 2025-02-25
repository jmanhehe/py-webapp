from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/todos"

@app.route("/todos", methods=["GET"])
def get_todos():
    return render_template("index.html")

@app.route("/api/todos", methods=["GET"])
def api_todos():
    response = requests.get(JSONPLACEHOLDER_URL)
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Failed to fetch todos"}), 500

if __name__ == "__main__":
    app.run(debug=True)
