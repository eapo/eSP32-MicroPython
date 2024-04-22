print('\ninit main.py\n...')

import time
import machine
import esp32 # type: ignore
import os
import binascii

# Get the unique ID
unique_id = machine.unique_id()

# Decode the unique ID to hexadecimal representation
hex_unique_id = binascii.hexlify(unique_id).decode('utf-8')

celsius = (esp32.raw_temperature() - 32) * 5.0 / 9.0

print("machine.reset_cause:",machine.reset_cause())
print("machine.unique_id:",machine.unique_id(),"|",hex_unique_id)
print("machine.freq:",machine.freq()/1000000,"MHz")
print("esp32.raw_temperature:",celsius,"C")

lsroot = os.listdir('/')
print("os.listdir('/'):")
for item in lsroot:
    if (os.stat(item)[0] == 16384):
        print("\t","/" + item + "/")
    else:
        print("\t","/" + item,str(os.stat(item)[6])+"b")

print('\nHello world!')




