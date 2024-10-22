
# Smart Home System IoT Project

Welcome to the Smart Home System IoT Project. To ensure a smooth implementation, please follow the instructions below carefully.

## Setting Up Edge Servers

1. **Create 3 Edge Servers:**
   - Ensure all edge devices are connected to the same WiFi network for reliable communication.
   - Use a Bridged Adapter for network connectivity when setting up the EDGE servers.

2. **Software Requirements:**
   - Ensure Python 3, MQTT, Paho, Flask, and Pip3 are installed on all three machines.

## Preparing the Code

1. **Unzip the provided “codes.zip” file:**
   - The archive contains three folders:
     1. Main Arduino – Nidula
     2. Sub Arduino 1 – Vihanga
     3. Sub Arduino 2 – Mark
   - Extract each folder to a separate machine.

## Running MQTT Scripts

1. **Main Machine:**
   - Open the terminal and run the following command:
     ```bash
     mosquitto_sub -h test.mosquitto.org -t nvm-main-arduino-topic
     ```

2. **Sub Arduino 1 Machine:**
   - Open the terminal and run:
     ```bash
     mosquitto_sub -h test.mosquitto.org -t nvm-sub-arduino-topic-v
     ```

3. **Sub Arduino 2 Machine:**
   - Open the terminal and run:
     ```bash
     mosquitto_sub -h test.mosquitto.org -t nvm-sub-arduino-topic-m
     ```

## Important Configuration for Debian Linux Users

1. **Configuring the Python Interpreter:**
   - Open Thonny Python IDE.
   - Click on the button at the bottom left labeled “local python 3 /usr/bin/python3”.
   - Click on “Configure Interpreter”.
   - Go to the “General” tab and uncheck “Allow Only Single Thonny Instance”.
   - Press OK and restart the IDE.

## Setting Up ThingsBoard

1. **Create 3 New Devices:**
   - On the ThingsBoard platform, create three new devices.

2. **Update Access Tokens and Device Names in “main_to_cloud.py”:**
   ```python
   device_tokens = {
       'T': '2hj0DuOWzNI6LqM3yFjl',
       'M': 'HM4E36xjHFWvJ6b09KnV',
       'L': '271FtNXZSU3HjXz8Jra9'
   }
   
   data = {'T': None, 'M': None, 'L': None}
   ```

3. **Run Scripts:**
   - On Sub Arduino 1 and Sub Arduino 2 machines, run:
     ```bash
     python3 sub_to_main.py
     ```
   - On the main Arduino machine, run:
     ```bash
     python3 main_to_cloud.py
     ```

4. **Create Visualizations:**
   - Create three visualizations of your choice on the ThingsBoard platform.
   - At this point, ThingsBoard should be operational.

## Running the Application

1. **Run “listener.py” on both Sub Arduino Machines:**
   ```bash
   python3 listener.py
   ```

2. **Run “app.py” on the main machine on localhost port 5000:**
   ```bash
   python3 app.py
   ```

   - The user interface should now be accessible and operational.

By following these steps, your Smart Home System IoT Project should be fully functional. If you encounter any issues, double-check the configurations and ensure all dependencies are properly installed. Enjoy your smart home system!
