print('\n\033[1;32m' + 'init ws2815.py' + '\033[0m\n\033[5m🚥🚥🚥\033[0m')

# WS2815 controller for MicroPython
import time
import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(4), 150)

def demo(np):
    """
    Executes a series of animations on a NeoPixel strip.

    Args:
        np (neopixel.NeoPixel): The NeoPixel strip to animate.

    Returns:
        None

    This function performs three different animations on the NeoPixel strip:

    1. Cycle: The strip lights up one LED at a time in a cyclic order.
    2. Bounce: The strip lights up one LED at a time and moves it back and forth.
    3. Fade in/out: The strip lights up one LED at a time and fades in and out.

    After the animations are complete, the strip is cleared.

    Example usage:
        np = neopixel.NeoPixel(machine.Pin(4), 150)
        demo(np)
    """
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

demo(np)

print('\n🚥🚥🚥✅\n')