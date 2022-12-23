#!/usr/bin/python3

# test-button.py
# Ian Blake
#
# used to test Bluetooth connection to micro:bit device
# and button responses
# based on sample code from micro:bit BLE workshop by Barry Byford
# at https://ukbaz.github.io/howto/ubit_workshop.html


import asyncio
import time
from bluezero import microbit

ubit = microbit.Microbit(adapter_addr='DC:A6:32:5D:5E:84',
                         device_addr='F1:2D:C9:E4:DE:F4')

looping = True

ubit.connect()
time.sleep(1)

busy = 0
ubit.pixels = [0b11110, 0b10000, 0b11100, 0b10000, 0b10000]

def freebusy():
    global busy
    if ubit.button_a > 0:
        busy = 0
        ubit.pixels = [0b11110, 0b10000, 0b11100, 0b10000, 0b10000]
    elif ubit.button_b > 0:
        busy = 1
        ubit.pixels = [0b11100, 0b10010, 0b11100, 0b10010, 0b11100]

while looping:
    freebusy()
    print(busy)
    time.sleep(1)
