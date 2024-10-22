import serial
import subprocess

# Set up the serial connection
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
main_topic = 'nvm-main-arduino-topic'
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
            print(decoded_data)
            # Publish the data to the MQTT broker
            subprocess.run(['mosquitto_pub', '-h', 'test.mosquitto.org', '-t', main_topic, '-m', decoded_data])
except KeyboardInterrupt:
    print("Serial communication interrupted.")
finally:
    # Close the serial connection
    ser.close()
