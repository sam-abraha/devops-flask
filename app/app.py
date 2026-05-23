from flask import Flask, jsonify, request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "flask_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "http_status"]
)

REQUEST_LATENCY = Histogram(
    "flask_http_request_duration_seconds",
    "HTTP request latency",
    ["endpoint"]
)

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def record_metrics(response):
    latency = time.time() - request.start_time
    endpoint = request.path

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=endpoint,
        http_status=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(endpoint=endpoint).observe(latency)

    return response


@app.route("/")
def home():
    return jsonify({"message": "Hello Test"})

@app.route("/health")
def health():
    return jsonify({"status": "200"})

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)