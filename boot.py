print('\n\033[1;32m' + 'init boot.py' + '\033[0m\n\033[5m...\033[0m')

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

print("\033[32mConnected to Wi-Fi:\033[0m", wifi_ssid, wifi.ifconfig())
print("\033[32m")
import webrepl
webrepl.start()

print("WebREPL started\033[0m")