import network
import time
import machine
import dht
import urequests  # MicroPython library for HTTP requests
import os
from dotenv import load_dotenv

load_dotenv()

# Wi-Fi credentials
WIFI_SSID = os.getenv("WIFI_NAME", "")
WIFI_PASS = os.getenv("WIFI_PASS", "")

# Flask Server URL
FLASK_SERVER_URL = os.getenv("FLASK_SERVER_URL", "http://192.168.1.100:5000/data")  # Update with your server IP

# Sensor pins
TRIG_PIN = 14
ECHO_PIN = 12
DHT_PIN = 13

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    while not wlan.isconnected():
        pass
    print("Connected to Wi-Fi")

# Initialize sensors
dht_sensor = dht.DHT11(machine.Pin(DHT_PIN))
trig = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

# Function to measure distance
def get_distance():
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()
    
    pulse_time = machine.time_pulse_us(echo, 1, 30000)  # Timeout after 30ms
    if pulse_time < 0:
        return None  # No echo received
    
    distance = (pulse_time * 0.0343) / 2  # Convert to cm
    return round(distance, 2)

# Connect to Wi-Fi
connect_wifi()

while True:
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    distance = get_distance()
    
    is_warning = 1 if temperature > 35 or temperature < 15 else 0
    
    payload = {
        "temperature": temperature,
        "humidity": humidity,
        "distance": distance if distance is not None else 0,
        "is_warning": is_warning
    }
    
    print("Sending data:", payload)
    try:
        response = urequests.post(FLASK_SERVER_URL, json=payload)
        print("Response:", response.text)
        response.close()
    except Exception as e:
        print("Error sending data:", e)
    
    time.sleep(5)
