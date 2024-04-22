print('\n\033[1;32m' + 'init main.py' + '\033[0m\n\033[5m...\033[0m')

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

print("\033[32mmachine.reset_cause:\033[0m\t",machine.reset_cause())
print("\033[32mmachine.unique_id:\033[0m\t",machine.unique_id(),"\033[32m|\033[0m",hex_unique_id)
print("\033[32mmachine.freq:\033[0m\t\t",machine.freq()/1000000,"MHz")
print("\033[32mesp32.raw_temperature:\033[0m\t",celsius,"C")

lsroot = os.listdir('/')
print("\033[32mos.listdir('/'):\033[0m\t",len(lsroot),"items")
for item in lsroot:
    if (os.stat(item)[0] == 16384):
        print(" 📁","/\033[0;97m" + item + "\033[0m/")
    else:
        print(" 📄","/" + item,str(os.stat(item)[6]) + "b")

print('\n\033[1;97m🖖🤖🐍\033[0m\n')
