#!/bin/bash

# the interface of the access point
AP_INTERFACE="wlan0"
# the SSID of the access point
AP_SSID="JetsonAP"
# the password of the access point
AP_PASSWORD="password"

# stop NetworkManager
sudo systemctl stop NetworkManager

# check if the access point is already running and stop services
if systemctl is-active --quiet hostapd; then
    sudo systemctl stop hostapd
    sudo systemctl stop dnsmasq
fi

# clean up the previous configuration
sudo ip link set $AP_INTERFACE down
sudo ip addr flush dev $AP_INTERFACE

# configure the access point
sudo ip link set $AP_INTERFACE up
sudo ip addr add 192.168.42.1/24 dev $AP_INTERFACE

# configure dnsmasq
echo -e "interface=$AP_INTERFACE\n\
dhcp-range=192.168.42.10,192.168.42.50,255.255.255.0,12h" | sudo tee /etc/dnsmasq.conf

# configure hostapd
echo -e "interface=$AP_INTERFACE\n\
ssid=$AP_SSID\n\
hw_mode=g\n\
channel=7\n\
wmm_enabled=0\n\
macaddr_acl=0\n\
auth_algs=1\n\
ignore_broadcast_ssid=0\n\
wpa=2\n\
wpa_passphrase=$AP_PASSWORD\n\
wpa_key_mgmt=WPA-PSK\n\
wpa_pairwise=TKIP\n\
rsn_pairwise=CCMP" | sudo tee /etc/hostapd/hostapd.conf

# ensure hostapd uses the correct config file
sudo sed -i 's|#DAEMON_CONF=""|DAEMON_CONF="/etc/hostapd/hostapd.conf"|' /etc/default/hostapd

# enable and start dnsmasq and hostapd
sudo systemctl enable --now dnsmasq
sudo systemctl enable --now hostapd

