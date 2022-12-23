# Are You Free?

### Ian Blake

## Overview

When you're working from home, it's very easy to be disturbed by others. My idea is to create an online "do not disturb" system that can tell when you're busy in a Zoom meeting, on a phone call, or recording your latest YouTube video, so that those who live with you know that it mightn't be a good time to interrupt you.

## Tools, Technologies and Equipment

A Raspberry Pi 4 runs the main script for this project.

Each user would have a BBC micro:bit to monitor sound in their room. When this device detects sound for more than five seconds, it would set a flag to say that the user is busy. This flag would be reset sixty seconds after they stop detecting sound (to allow for pauses).

These BBC micro:bits would connect to the Raspberry Pi server via Bluetooth. These devices have microphones and small LED displays built in. The micro:bits would send the free/busy data to the Pi via UART and would allow users to manually set their status using the buttons on the device.

The Raspberry Pi would also scan the local network to see if the user's laptop is connected to the local network.

Each user's status, i.e. free/busy and offline/online, would be displayed on a .

The main language used for the project will be Python. The web page would use Javascript to 

## Project Repository

The project is hosted at [https://github.com/ianbl8/areyoufree](https://github.com/ianbl8/areyoufree)

## Issues

The project is currently incomplete due to the following issues:

1. Micro:bits can only use Bluetooth if programmed through the online service, [https://makecode.microbit.org/](Makecode). The Python version of the final code is in the repository along with the hexcode file.

2. There were some Bluetooth connection issues with the micro:bits. Also these devices need to be removed from and re-paired to the Rasperry Pi whenever they were flashed with a new hexcode file.

3. In testing, the Raspberry Pi could receive the free/busy data from the Raspberry Pi via UART, and it could print this to the console within a callback function, but this data could not be accessed outside of the callback function. Using the buttons became the only way to record a user's free/busy status.

4. The nmap service crashed regularly, also crashing the SSH terminal connection between my Windows laptop and the Raspberry Pi. Nmap also failed to find my laptop on occasion even though it was online.

5. Despite being connected (finally) to the MQTT broker via websockets, the MQTT script in the (web page)[http://areyoufree.glitch.me/index.html] did not seem to subscribe properly or receive any messages. 
