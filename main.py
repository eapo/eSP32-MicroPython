print('\n\033[1;32m' + 'init main.py' + '\033[0m\n\033[5m...\033[0m')

import time
import machine
import esp32 # type: ignore
import os
import binascii
import uos

# Read the current counter value from the file
with open('/counter.txt', 'r') as f:
    counter = int(f.read())

# Increment the counter
counter += 1

# Get the unique ID
unique_id = machine.unique_id()

# Decode the unique ID to hexadecimal representation
hex_unique_id = binascii.hexlify(unique_id).decode('utf-8')

celsius = (esp32.raw_temperature() - 32) * 5.0 / 9.0

print("\033[32mmachine.reset_cause:\033[0m\t",machine.reset_cause())
print("\033[32mmachine.unique_id:\033[0m\t",machine.unique_id(),"\033[32m|\033[0m",hex_unique_id)
print("\033[32mmachine.freq:\033[0m\t\t",machine.freq()/1000000,"MHz")
print("\033[32mesp32.raw_temperature:\033[0m\t",celsius,"C")

# List the files in the root directory
lsroot = os.listdir('/')
print("\033[32mos.listdir('/'):\033[0m\t",len(lsroot),"items\t\033[32m# lsroot\033[0m")
if (counter < 2):
    for item in lsroot:
        if (os.stat(item)[0] == 16384):
            print(" 📁","/\033[0;97m" + item + "\033[0m/")
        else:
            print(" 📄","/" + item,str(os.stat(item)[6]) + "b")

    print('\n\033[1;97m🖖🤖🐍\033[0m\n')

# Write the updated counter value back to the file
with open('/counter.txt', 'w') as f:
    f.write(str(counter))

print("\033[32mInit counter:\t\033[0m", counter, '\t\033[32m# exec(open(\'/main.py\').read())\033[0m\n')

# init 1st univere
exec(open('/1st.py').read())
