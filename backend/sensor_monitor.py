from datetime import datetime, timedelta


SENSOR_TIMEOUT_SECONDS = 15

last_seen = {}


def update_sensor(sensor_id):
    last_seen[sensor_id] = datetime.now()


def get_sensor_status(sensor_id):

    if sensor_id not in last_seen:
        return {
            "sensor_id": sensor_id,
            "status": "UNKNOWN"
        }

    elapsed = (
        datetime.now() - last_seen[sensor_id]
    ).total_seconds()

    if elapsed > SENSOR_TIMEOUT_SECONDS:
        return {
            "sensor_id": sensor_id,
            "status": "OFFLINE",
            "seconds_since_last_reading": round(elapsed, 2),
            "alert": True
        }

    return {
        "sensor_id": sensor_id,
        "status": "ONLINE",
        "seconds_since_last_reading": round(elapsed, 2),
        "alert": False
    }