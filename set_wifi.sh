#!/bin/bash

# the interface of the WiFi client
WIFI_INTERFACE="wlan0"

# wait for the file to be created
while [ ! -f /path/to/file ]; do
    sleep 1
done

# read the SSID and password from the file
readarray -t lines < /path/to/file
SSID="${lines[0]}"
PASSWORD="${lines[1]}"

# create the WiFi connection
nmcli dev wifi con "$SSID" password "$PASSWORD" ifname $WIFI_INTERFACE
