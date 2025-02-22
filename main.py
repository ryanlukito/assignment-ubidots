import network
import time
import machine
import dht
import os
from umqtt.simple import MQTTClient
from dotenv import load_dotenv

load_dotenv()

# Wi-Fi credentials
WIFI_SSID = os.getenv("WIFI_NAME", "")
WIFI_PASS = os.getenv("WIFI_PASS", "")

# Ubidots credentials
UBIDOTS_TOKEN = os.getenv("UBIDOTS_TOKEN", "")
MQTT_BROKER = os.getenv("MQTT_BROKER", "industrial.api.ubidots.com")
MQTT_PORT = 1883
DEVICE_LABEL = os.getenv("DEVICE_LABEL", "esp32_device")
TOPIC = f"/v1.6/devices/{DEVICE_LABEL}"

# Sensor pins
TRIG_PIN = 14
ECHO_PIN = 12
DHT_PIN = 13

# Setup Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    while not wlan.isconnected():
        pass
    print("Connected to Wi-Fi")

# Setup MQTT client
client = MQTTClient("esp32", MQTT_BROKER, port=MQTT_PORT, user=UBIDOTS_TOKEN, password="", keepalive=60)

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

# Connect to Wi-Fi and MQTT
connect_wifi()
client.connect()

while True:
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    distance = get_distance()
    
    is_warning = 1 if temperature > 35 or temperature < 15 else 0
    
    payload = {
        "temperature_data": {"value": temperature},
        "humidity_data": {"value": humidity},
        "distance_data": {"value": distance if distance is not None else 0},
        "is_warning": {"value": is_warning}
    }
    
    print("Sending data:", payload)
    client.publish(TOPIC, str(payload).replace("'", '"'))  # Convert to JSON format
    time.sleep(5)