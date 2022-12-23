#!/usr/bin/python3

# areyoufree.py
# Ian Blake
#
# used for Bluetooth connections to 2 micro:bit devices
# and button responses from each device
# calling a script to detect devices on LAN


import json
import time
from bluezero import microbit
import scripts.presence_detector

# ubit1: red micro:bit (vitop)
ubit1 = microbit.Microbit(adapter_addr='DC:A6:32:5D:5E:84',
                         device_addr='FE:4C:62:F3:26:65')
# ubit2: yellow micro:bit (vuviv)
ubit2 = microbit.Microbit(adapter_addr='DC:A6:32:5D:5E:84',
                         device_addr='F1:2D:C9:E4:DE:F4')

looping = True

# connect to micro:bits
print("Connecting to micro:bits")
ubit1.connect()
ubit2.connect()
time.sleep(1)

# set devices to Free
busy1 = False
busy2 = False
online1 = False
online2 = False
online1check = 0
online2check = 0
ubit1.pixels = [0b11110, 0b10000, 0b11100, 0b10000, 0b10000] # F
ubit2.pixels = [0b11110, 0b10000, 0b11100, 0b10000, 0b10000] # F

# detect button presses and set free/busy
def checkbusy():
    global busy1, busy2
    if ubit1.button_a > 0:
        busy1 = False
        ubit1.pixels = [0b11110, 0b10000, 0b11100, 0b10000, 0b10000] # F
    elif ubit1.button_b > 0:
        busy1 = True
        ubit1.pixels = [0b11100, 0b10010, 0b11100, 0b10010, 0b11100] # B
    if ubit2.button_a > 0:
        busy2 = False
        ubit2.pixels = [0b11110, 0b10000, 0b11100, 0b10000, 0b10000] # F
    elif ubit2.button_b > 0:
        busy2 = True
        ubit2.pixels = [0b11100, 0b10010, 0b11100, 0b10010, 0b11100] # B

def checkonline():
    global online1, online2, online1check, online2check
    devices_found = scripts.presence_detector.find_devices()
    # check for devices and allow for missed scans
    if 'user1' in str(devices_found):
        online1check = 5
    else:
        online1check -= 1
    if 'user2' in str(devices_found):
        online2check = 5
    else:
        online2check -= 1
    # update device statuses
    if online1check > 0:
        online1 = True
    else:
        online1check = 0
        online1 = False
    if online2check > 0:
        online2 = True
    else:
        online2check = 0
        online2 = False

# display free/busy for each device
while looping:
    checkbusy()
    checkonline()
    time.sleep(0.1)
    print(f'User 1: Busy, {busy1}; Online, {online1} | User 2: Busy, {busy2}; Online, {online2}') # turn to JSON 
    

