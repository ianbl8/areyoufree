#!/usr/bin/python3
#coding=utf-8

# presence_detector.py
# Ian Blake
#
# used to detect users devices on LAN
# based on sample code from Week 8 Lab on MQTT

import subprocess

# Dictionary of known devices
# Used to match devices to users
devices = [
    {"name":"user1", "mac":"30:03:C8:54:D1:21"},
    {"name":"user2", "mac":"C8:FF:28:B5:FA:CB"}
]

# Return list of known devices on LAN
def find_devices():
    output = subprocess.check_output("sudo nmap -sn 192.168.0.0/24 | grep MAC", shell=True)
    devices_found = []
    for dev in devices:
        if dev["mac"].lower() in str(output).lower():
            devices_found.append(dev)
    return devices_found

# Main program
def main():
    print(find_devices())

if __name__ == "__main__":
    main()