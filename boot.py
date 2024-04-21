print('\ninit boot.py\n...')

import config  # Import configuration file
import network
import time

# Connect to WiFi using the configurations from config.py
wifi_ssid = config.wifi_ssid
wifi_password = config.wifi_password

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(wifi_ssid, wifi_password)

# Wait until connected
while not wifi.isconnected():
    time.sleep(1)

print("Connected to Wi-Fi:", wifi_ssid, wifi.ifconfig())

import webrepl
webrepl.start()

print("WebREPL started")