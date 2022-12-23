#!/usr/bin/python3

# test2buttons.py
# Ian Blake
#
# used to test Bluetooth connections to 2 micro:bit devices
# and button responses from each device
# based on sample code from micro:bit BLE workshop by Barry Byford
# at https://ukbaz.github.io/howto/ubit_workshop.html


import asyncio
import time
from bluezero import microbit

# ubit1: red micro:bit (vitop)
ubit1 = microbit.Microbit(adapter_addr='DC:A6:32:5D:5E:84',
                         device_addr='FE:4C:62:F3:26:65')
# ubit2: yellow micro:bit (vuviv)
ubit2 = microbit.Microbit(adapter_addr='DC:A6:32:5D:5E:84',
                         device_addr='F1:2D:C9:E4:DE:F4')

looping = True

ubit1.connect()
ubit2.connect()
time.sleep(1)

busy1 = 0
busy2 = 0
ubit1.pixels = [0b11110, 0b10000, 0b11100, 0b10000, 0b10000]
ubit2.pixels = [0b11110, 0b10000, 0b11100, 0b10000, 0b10000]

def freebusy():
    global busy1, busy2
    if ubit1.button_a > 0:
        busy1 = 0
        ubit1.pixels = [0b11110, 0b10000, 0b11100, 0b10000, 0b10000]
    elif ubit1.button_b > 0:
        busy1 = 1
        ubit1.pixels = [0b11100, 0b10010, 0b11100, 0b10010, 0b11100]
    if ubit2.button_a > 0:
        busy2 = 0
        ubit2.pixels = [0b11110, 0b10000, 0b11100, 0b10000, 0b10000]
    elif ubit2.button_b > 0:
        busy2 = 1
        ubit2.pixels = [0b11100, 0b10010, 0b11100, 0b10010, 0b11100]

while looping:
    freebusy()
    print(f'Device 1: {busy1} | Device 2: {busy2}')
    time.sleep(1)
