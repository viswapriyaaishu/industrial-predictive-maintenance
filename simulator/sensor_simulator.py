import random
import time
from datetime import datetime


MACHINE_ID = "MACHINE_001"
SENSOR_ID = "SENSOR_001"


def generate_reading():
    vibration = round(random.uniform(2.0, 4.0), 2)
    temperature = round(random.uniform(45.0, 60.0), 2)
    pressure = round(random.uniform(4.5, 6.0), 2)

    return {
        "machine_id": MACHINE_ID,
        "sensor_id": SENSOR_ID,
        "timestamp": datetime.now().isoformat(),
        "vibration": vibration,
        "temperature": temperature,
        "pressure": pressure
    }


def main():
    print("===================================")
    print(" Industrial IoT Sensor Simulator")
    print("===================================")
    print(f"Machine ID : {MACHINE_ID}")
    print(f"Sensor ID  : {SENSOR_ID}")
    print("Status     : ONLINE")
    print()

    while True:
        reading = generate_reading()

        print("-----------------------------------")
        print(f"Timestamp   : {reading['timestamp']}")
        print(f"Vibration   : {reading['vibration']} mm/s")
        print(f"Temperature : {reading['temperature']} °C")
        print(f"Pressure    : {reading['pressure']} bar")

        time.sleep(5)


if __name__ == "__main__":
    main()