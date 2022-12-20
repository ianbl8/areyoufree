# test2devices.py
# Ian Blake
#
# used to test simultaneous Bluetooth connections to 2 micro:bit devices
# based on sample code from micro:bit BLE workshop by Barry Byford
# at https://ukbaz.github.io/howto/ubit_workshop.html

import time
from bluezero import microbit

# ubit1: red micro:bit (vitop)
ubit1 = microbit.Microbit(adapter_addr='DC:A6:32:5D:5E:84',
                         device_addr='FE:4C:62:F3:26:65')
# ubit2: yellow micro:bit (vuviv)
ubit2 = microbit.Microbit(adapter_addr='DC:A6:32:5D:5E:84',
                         device_addr='F1:2D:C9:E4:DE:F4')

ubit1.connect()
ubit2.connect()

while ubit1.button_a < 1:
    ubit1.pixels = [0b00000, 0b01000, 0b11111, 0b01000, 0b00000]
    time.sleep(0.5)
    ubit1.clear_display()

while ubit2.button_a < 1:
    ubit2.pixels = [0b00000, 0b01000, 0b11111, 0b01000, 0b00000]
    time.sleep(0.5)
    ubit2.clear_display()

while ubit1.button_b < 1:
    ubit1.pixels = [0b00000, 0b00010, 0b11111, 0b00010, 0b00000]
    time.sleep(0.5)
    ubit1.clear_display()

while ubit2.button_b < 1:
    ubit2.pixels = [0b00000, 0b00010, 0b11111, 0b00010, 0b00000]
    time.sleep(0.5)
    ubit2.clear_display()

ubit1.disconnect()
ubit2.disconnect()