# Are You Free?

### Ian Blake

## Overview

When you're working from home, it's very easy to be disturbed by others. My idea is to create an online "do not disturb" system that can tell when you're busy in a Zoom meeting, on a phone call, or recording your latest YouTube video, so that those who live with you know that it mightn't be a good time to interrupt you.

## Tools, Technologies and Equipment

A Raspberry Pi 4 would be the main server for the project. This device would run the service and host the webpage showing the users and their statuses.

Each user would have a small device to monitor sound in their room. When this device detects sound for more than five seconds, it would set a flag to say that the user is busy. This flag would be reset sixty seconds after they stop detecting sound (to allow for pauses).

These devices will ideally be BBC micro:bits connected to the Raspberry Pi server via Bluetooth. These devices have microphones and small LED displays built in. (As an alternative, Raspberry Pi Zeros with microphones and LEDs could be used.)

The server would check with these devices to see if the user is busy. It would also check to see if the user's laptop or smartphone is connected to the local network.

There would be a webpage to show each user's status, i.e. free/busy and offline/online. A user would also be able to click a button on the page to change their status manually.

The main language used for the project will be Python.

## Project Repository

The project will be hosted at [https://github.com/ianbl8/areyoufree](https://github.com/ianbl8/areyoufree) (TBC - the project name is subject to change)
