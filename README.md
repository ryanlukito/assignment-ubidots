# UBIDOTS ASSIGNMENTS

## Project Overview

This project focuses on IoT dashboard monitoring using **Ubidots**. The system collects and monitors real-time sensor data, including:

- **Distance Data**
- **Temperature Data**
- **Humidity Data**

The collected data is essential for efficient monitoring and analysis, allowing users to track environmental conditions effectively.

---

## Project Collaborators

The following individuals are collaborating on this project:

| Name                      | Email                                     |
| ------------------------- | ----------------------------------------- |
| **Alex Cinatra Hutasoit** | acinatra@gmail.com                        |
| **Ryan Krishandi Lukito** | ryankrishandilukito@mail.ugm.ac.id        |
| **M Fachrizal Giffari**   | muhammad.fachrizal.giffari@mail.ugm.ac.id |
| **Mahsa Quereda Bahjah**  | mahsaqueredabahjah@mail.ugm.ac.id         |

---

## Features

- **Real-time monitoring** of distance, temperature, and humidity data
- **Dashboard visualization** via Ubidots
- **Automated data collection** for better insights

---

## How To Use

To run this project using Python, follow these steps:

1. **Install Dependencies:**

   ```sh
   pip install requests ubidots
   ```

2. **Set Up Ubidots API Key:**
   Replace `YOUR_UBIDOTS_API_KEY` with your actual API key in the script.

3. **Run the Python Script:**

   ```sh
   python main.py
   ```

4. **Monitor Data on Ubidots:**
   Log in to your Ubidots account and view the real-time data dashboard.

---

## In .env

Ensure your `.env` file contains the following credentials:

```sh
# Wi-Fi credentials
WIFI_SSID = os.getenv("WIFI_NAME", "")
WIFI_PASS = os.getenv("WIFI_PASS", "")

# Ubidots credentials
UBIDOTS_TOKEN = os.getenv("UBIDOTS_TOKEN", "")
MQTT_BROKER = os.getenv("MQTT_BROKER", "industrial.api.ubidots.com")
MQTT_PORT = 1883
DEVICE_LABEL = os.getenv("DEVICE_LABEL", "esp32_device")
TOPIC = f"/v1.6/devices/{DEVICE_LABEL}"
```

## Ubidots Interface

![Ubidots Page](<ubidots 1.jpg>)
![Ubidots Page](<ubidots 2.jpg>)

## Ubidots Link
[Link to our Ubidots Page](https://stem.ubidots.com/app/dashboards/public/dashboard/BkLWvZVUGWjgPIJnWnbKmlfxWoDZT0bgUfqOu6XuBjQ?navbar=true&contextbar=true&datePicker=true&devicePicker=true&displayTitle=true)
