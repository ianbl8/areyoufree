#!/usr/bin/python3

# test-uart.py
# Ian Blake
#
# used to test Bluetooth UART connection to micro:bit device
# based on sample code from micro:bit BLE workshop by Barry Byford
# at https://github.com/ukBaz/python-bluezero/issues/264

import time
from bluezero import microbit
from bluezero import async_tools
i_value = 0

# ubit2: yellow micro:bit (vuviv)
ubit2 = microbit.Microbit(adapter_addr='DC:A6:32:5D:5E:84',
                         device_addr='F1:2D:C9:E4:DE:F4')

# process data received
def handle_value(value):
    global i_value
    u_key, u_value = value.split(':')
    i_value = int(float(u_value))
    print(f'{u_key} = {i_value}')

eloop = async_tools.EventLoop()

ubit2.connect()

ubit2.subscribe_uart(handle_value)

ubit2.run_async()