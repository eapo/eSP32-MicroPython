print('\n\033[1;32m' + 'init ws2815.py' + '\033[0m\n\033[5m🚥🚥🚥\033[0m')

# WS2815 controller for MicroPython
import time
import machine
import neopixel

n = 150 # number of LEDs on ws2815
p = 4   # esp32 pin for ws2815

np = neopixel.NeoPixel(machine.Pin(p), n)

def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()

def set_color(r, g, b):
  for i in range(n):
    np[i] = (r, g, b)
  np.write()

print('\n\033[1;32m' + 'RGB order testing' + '\033[0m\n\033[5m🚥🚥🚥\033[0m')
for i in range(n):
    np[i-1] = (i, 0, 0)
    np.write()
    time.sleep(0.01)
for i in range(n):
    np[i-1] = (0, i, 0)
    np.write()
    time.sleep(0.01)
for i in range(n):
    np[i-1] = (0, 0, i)
    np.write()
    time.sleep(0.01)
for i in range(n):
    np[i-1] = (0, 0, 0)
    np.write()
    time.sleep(0.01)
    
for i in range(3):
    clear()
    time.sleep(0.01)
    np[0] = (10, 10, 10)
    np[1] = (10, 0, 0)
    np[2] = (0, 10, 0)
    np[3] = (0, 0, 10)
    np[n-1] = (255, 255, 255)
    np[n-2] = (255, 255, 255)
    np[n-3] = (255, 255, 255)
    np.write()
    time.sleep(0.01)

print('\n🚥🚥🚥✅\n')