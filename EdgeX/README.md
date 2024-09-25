The EdgeX IoT Gateway existed on a virtual machine.

The below image is to assist you on understanding the sequence flow between the IoT Sensor and processes on the virtual machine. 

![image](https://github.com/user-attachments/assets/9df76329-e7b0-4c54-9ef9-3ac911de0919)

This virtual machine runs several Docker containers and processes related to the IoT Honeypot Environment.

Functions:
-	EdgeX IoT Gateway: Collects traffic from the edge devices.
-	Docker Containers: Includes services such as Eclipse Mosquitto (MQTT broker), Telegraf (data collection agent), InfluxDB (time-series database), and Grafana (data visualization tool).
-	Processes and visualizes the data for analysis.
-	Monitors IoT Sensor.

Note: This virtual machine was not accessible via the internet. It only has an internal IP address. 
