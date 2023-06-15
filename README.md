# JetsonWiFiManager

### Overview

This project contains two scripts:

- `ap.sh`:
    - Creates an access point on the Jetson
- `server.py`
  - Runs a web server on the Jetson which allows us to input the SSID and password of the network we want to connect to
  - The Jetson will then connect to that network and the access point will be disabled

Once connected to the AP, connect to the web server by going to `http://192.168.42.1`
