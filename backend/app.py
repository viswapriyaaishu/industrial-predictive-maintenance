from flask import Flask, request, jsonify
from datetime import datetime

from model import predict_failure
from sensor_monitor import update_sensor, get_sensor_status

app = Flask(__name__)

latest_readings = {}


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "predictive-maintenance-api"
    })


@app.route("/telemetry", methods=["POST"])
def telemetry():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No telemetry data received"
        }), 400

    required_fields = [
        "machine_id",
        "sensor_id",
        "vibration",
        "temperature",
        "pressure"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Missing field: {field}"
            }), 400

    machine_id = data["machine_id"]
    sensor_id = data["sensor_id"]

    update_sensor(sensor_id)

    latest_readings[sensor_id] = {
        "machine_id": machine_id,
        "timestamp": datetime.now().isoformat(),
        "vibration": data["vibration"],
        "temperature": data["temperature"],
        "pressure": data["pressure"]
    }

    return jsonify({
        "message": "Telemetry received",
        "sensor_id": sensor_id
    }), 200


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No sensor data received"
        }), 400

    required_fields = [
        "vibration",
        "temperature",
        "pressure"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Missing field: {field}"
            }), 400

    result = predict_failure(
        data["vibration"],
        data["temperature"],
        data["pressure"]
    )

    return jsonify(result)

@app.route("/sensor-status", methods=["GET"])
def sensor_status():

    return jsonify({
        "sensors": latest_readings
    })


@app.route("/sensor-status/<sensor_id>", methods=["GET"])
def check_sensor(sensor_id):

    status = get_sensor_status(sensor_id)

    return jsonify(status)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )