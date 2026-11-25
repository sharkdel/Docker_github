import os
import requests
from flask import Flask, jsonify, request 

app = Flask(__name__)

@app.route('/fact')
def fact():
    r = requests.get("https://catfact.ninja/fact", timeout=10)
    r.raise_for_status()
    return jsonify(r.json())

@app.route("/fact/count")
def fact_count():
    # читаем параметр из URL: /fact/count?n=3
    from flask import request
    n = int(request.args.get("n", 1))
    facts = []
    for _ in range(n):
        r = requests.get("https://catfact.ninja/fact", timeout=10)
        r.raise_for_status()
        facts.append(r.json()["fact"])
    return jsonify({"count": n, "facts": facts})

@app.route("/")
def index():
    return "Cat Fact API. Иди в /fact"


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)