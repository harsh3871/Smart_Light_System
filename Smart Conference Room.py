import json
import random
import time
from datetime import datetime

# Azure IoT Device Client (optional if testing direct upload)
from azure.iot.device import IoTHubDeviceClient

# Azure IoT Hub Device Connection String
CONNECTION_STRING = "HostName=SmartLight.azure-devices.net;DeviceId=conferenceRoomLighting;SharedAccessKey=mxb34aYbu+VHKLEFx6nZnjXy0X3zdUDTOkiwy+dLCNE="

def send_to_azure(message):
    """Send data to Azure IoT Edge"""
    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        client.connect()
        client.send_message(json.dumps(message))
        print(f"Message sent: {message}")
        client.disconnect()
    except Exception as e:
        print(f"Failed to send message to Azure: {e}")

# Fake Data Generation Configuration
FAKE_DATA_DURATION = 60  # Total duration to generate fake data in seconds
LIGHT_TIMEOUT = 200       # Time in seconds before turning off lights without motion

def generate_fake_data():
    """Generate fake sensor data for testing"""
    light_status = False
    last_motion_time = time.time()

    try:
        print("Generating fake data...")
        for _ in range(FAKE_DATA_DURATION):
            current_time = time.time()

            # Simulate motion detection randomly (20% chance per second)
            motion_detected = random.random() < 0.2

            if motion_detected:
                last_motion_time = current_time
                light_status = True  # Turn on the light when motion is detected

            # Turn off light if no motion is detected for LIGHT_TIMEOUT seconds
            if light_status and (current_time - last_motion_time > LIGHT_TIMEOUT):
                light_status = False

            # Generate data packet
            data = {
                "timestamp": datetime.now().isoformat(),
                "motion_detected": motion_detected,
                "light_status": "on" if light_status else "off",
            }

            # Send or print data
            send_to_azure(data)  # Uncomment to send data to Azure
            print(json.dumps(data, indent=4))  # For local testing

            time.sleep(1)  # Generate data every second

    except KeyboardInterrupt:
        print("Data generation stopped.")

if __name__ == "__main__":
    generate_fake_data()