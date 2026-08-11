import random
import time

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    time.sleep(random.uniform(0.05, 0.2))

    return jsonify(
        service="sre-demo-service",
        status="running"
    )


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


@app.route("/work")
def work():
    processing_time = random.uniform(0.1, 0.5)
    time.sleep(processing_time)

    return jsonify(
        status="completed",
        processing_time=round(processing_time, 3)
    )

@app.route("/error")
def error():
    return jsonify(
        status="error",
        message="Simulated internal server error"
    ), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)