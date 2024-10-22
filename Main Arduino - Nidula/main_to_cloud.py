import serial
import subprocess
import paho.mqtt.client as mqtt

# ThingsBoard device tokens
device_tokens = {
    'T': '2hj0DuOWzNI6LqM3yFjl',
    'M': 'HM4E36xjHFWvJ6b09KnV',
    'L': '271FtNXZSU3HjXz8Jra9'
}

# Set up the serial connection
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

# MQTT Broker settings
mqtt_broker = 'test.mosquitto.org'
mqtt_topic = 'nvm-main-arduino-topic'

# Initialize a dictionary to store data
data = {'T': None, 'M': None, 'L': None}

# Function to publish data to ThingsBoard
def publish_to_thingsboard(device, value):
    if device in device_tokens:
        token = device_tokens[device]
        topic = 'v1/devices/me/telemetry'
        message = f'{{"{device}":{value}}}'
        command = [
            'mosquitto_pub', '-d', '-q', '1',
            '-h', 'mqtt.thingsboard.cloud', '-p', '1883',
            '-t', topic, '-u', token, '-m', message
        ]
        subprocess.run(command)
    else:
        print(f"Key '{device}' not found in device_tokens dictionary.")

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    print(f"MQTT Message received: {msg.payload.decode()}")
    raw_data = msg.payload.decode().strip()
    key, value = raw_data.strip('{}').split(':')

    if key in device_tokens:
        data[key] = value
        publish_to_thingsboard(key, value)
    else:
        print(f"Key '{key}' not found in device_tokens dictionary.")

# Set up MQTT client
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(mqtt_broker, 1883, 60)
mqtt_client.loop_start()

try:
    while True:
        if ser.in_waiting > 0:
            # Read the line from the serial port
            raw_data = ser.readline()
            try:
                # Attempt to decode the data
                decoded_data = raw_data.decode('utf-8').rstrip()
            except UnicodeDecodeError:
                # Handle decoding errors by ignoring or replacing undecodable bytes
                decoded_data = raw_data.decode('utf-8', errors='ignore').rstrip()
                print("Warning: Decoding error occurred. Data was partially lost.")
            print(f"Serial Data received: {decoded_data}")
            key, value = decoded_data.strip('{}').split(':')
            if key in device_tokens:
                data[key] = value
                publish_to_thingsboard(key, value)
            else:
                print(f"Key '{key}' not found in device_tokens dictionary.")
except KeyboardInterrupt:
    print("Serial communication interrupted.")
finally:
    # Close the serial connection
    ser.close()
    mqtt_client.loop_stop()
    mqtt_client.disconnect()