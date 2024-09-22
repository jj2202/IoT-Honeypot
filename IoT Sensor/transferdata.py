import sys
import time
import requests
import json
import pymysql.cursors
from sense_hat import SenseHat
from azure.iot.device import IoTHubDeviceClient, Message

# Define EdgeX Foundry IP address
edgexip = "192.168.10.110"

# Define the connection string for your Azure IoT Hub device
CONNECTION_STRING = "<Your Device Connection String>"

# Database connection parameters
db_config = {
    'host': '192.168.10.12',
    'user': 'FYP',
    'password': 'fyp123',
    'db': 'fyp',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# Initialize Sense HAT
sense = SenseHat()

# Define EdgeX Foundry API endpoints
urlTemp = f'http://{edgexip}:49986/api/v1/resource/Temp_and_Humidity_Sensor_Cluster/temperature'
urlHum = f'http://{edgexip}:49986/api/v1/resource/Temp_and_Humidity_Sensor_Cluster/humidity'

# Define headers for HTTP requests
headers = {'content-type': 'application/json'}

# Initialize the IoT Hub client
def create_azure_client():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

# Send data to Azure IoT Hub
def send_to_azure(client, temperature, humidity):
    data = {
        "temperature": temperature,
        "humidity": humidity
    }
    message = Message(json.dumps(data))
    client.send_message(message)
    print(f"Data sent to Azure IoT Hub: {data}")

# Insert data into MySQL database
def insert_into_mysql(temperature, humidity):
    try:
        connection = pymysql.connect(**db_config)
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO datas (date, time, temperature, humidity) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (time.strftime("%Y-%m-%d"), time.strftime("%H:%M:%S"), temperature, humidity))
            connection.commit()
        except pymysql.MySQLError as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            connection.close()
    except pymysql.MySQLError as e:
        print(f"Connection error: {e}")

# Send data to EdgeX Foundry
def send_to_edgex(temperature, humidity):
    try:
        response_temp = requests.post(urlTemp, data=json.dumps(int(temperature)), headers=headers, verify=False)
        response_hum = requests.post(urlHum, data=json.dumps(int(humidity)), headers=headers, verify=False)

        if response_temp.status_code == 200 and response_hum.status_code == 200:
            print(f"Data sent to EdgeX Foundry - Temperature: {temperature}°C, Humidity: {humidity}%")
        else:
            print("Failed to send data to EdgeX Foundry")
    except requests.exceptions.RequestException as e:
        print(f"EdgeX error: {e}")

def main():
    azure_client = create_azure_client()

    while True:
        try:
            # Read temperature and humidity from Sense HAT
            temperature = round(sense.get_temperature(), 2)
            humidity = round(sense.get_humidity(), 2)

            if temperature is not None and humidity is not None:
                # Send data to EdgeX Foundry
                send_to_edgex(temperature, humidity)

                # Insert data into MySQL database
                insert_into_mysql(temperature, humidity)

                # Send data to Azure IoT Hub
                send_to_azure(azure_client, temperature, humidity)

                print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
            else:
                print("Failed to read data from Sense HAT")
        except Exception as e:
            print(f"Error: {e}")

        # Wait before reading data again
        time.sleep(2)

if __name__ == "__main__":
    main()
