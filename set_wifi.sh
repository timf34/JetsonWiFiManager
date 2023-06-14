#!/bin/bash

# the interface of the WiFi client
WIFI_INTERFACE="wlan0"

# wait for the file to be created
while [ ! -f /tmp/wifi_credentials ]; do
    sleep 1
done

# read the SSID and password from the file
readarray -t lines < /tmp/wifi_credentials
SSID="${lines[0]}"
PASSWORD="${lines[1]}"

# try to connect to the WiFi network
if nmcli dev wifi con "$SSID" password "$PASSWORD" ifname $WIFI_INTERFACE; then
    # if successful, stop the access point and dnsmasq
    sudo systemctl stop hostapd
    sudo systemctl stop dnsmasq
else
    # if failed, remove the file so the access point is created on the next boot
    rm /path/to/file
fi
