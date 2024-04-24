print('\n\033[1;32m' + 'init artnet.py' + '\033[0m\n\033[5m🚥🚥🚥\033[0m')

from stupidArtnet import StupidArtnetServer
import time

addr = 0

def dmx2ws2815(data):
    # print('DMX data: ', data)
    # np[42] = (data[0], data[1], data[2])
    for i in range(0, n):
        r = data[i * 3]
        g = data[i * 3 + 1]
        b = data[i * 3 + 2]
        np[i] = (r, g, b)
        # print('pixel', i, 'rgb(', r, g, b, ')')
    np.write()

# create a callback to handle data when received
def test_callback(data):
    """Test function to receive callback data."""
    # the received data is an array
    # of the channels value (no headers)
    # print('Received new data \n', data)

# a Server object initializes with the following data
# universe 			= DEFAULT 0
# subnet   			= DEFAULT 0
# net      			= DEFAULT 0
# setSimplified     = DEFAULT True
# callback_function = DEFAULT None

# You can use universe only
universe = 1
a = StupidArtnetServer()

# For every universe we would like to receive,
# add a new listener with a optional callback
# the return is an id for the listener
u1_listener = a.register_listener(
    universe, callback_function=dmx2ws2815)

# or disable simplified mode to use nets and subnets as per spec
# subnet = 1 (would have been universe 17 in simplified mode)
# net = 0
# a.register_listener(universe, sub=subnet, net=net,
#                    setSimplified=False, callback_function=test_callback)

# print object state
print('\033[1;32m')
print(a)
print('\033[0m')

# if you prefer not using callbacks, the channel data
# is also available in the method get_buffer()
# use the given id to access it
buffer = a.get_buffer(u1_listener)

# Remember to check the buffer size, as this may vary from 512
n_data = len(buffer)
print('\033[1;32m' + 'Buffer size:\t' + '\033[0m', n_data)
if n_data > 0:
    # in which channel 1 would be
    print('\033[1;32m' + 'Ch 1:\t' + '\033[0m', buffer[0])

    # and channel 20 would be
    print('\033[1;32m' + 'Ch 20:\t' + '\033[0m', buffer[19])

print('\033[1;32m' + 'DMX ready state 📲✅' + '\033[0m\n')

# Cleanup
del a