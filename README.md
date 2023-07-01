# JetsonWiFiManager

### Overview

This project contains three scripts:

- `run_wifi.sh`
  - This contains the other two scripts 
  - Make it executable by running `chmod +x run_wifi.sh`
  - Run it by running `sudo ./run_wifi.sh`
- `ap.sh`:
    - Creates an access point on the Jetson
- `server.py`
  - Runs a web server on the Jetson which allows us to input the SSID and password of the network we want to connect to
  - The Jetson will then connect to that network and the access point will be disabled

Once connected to the AP, connect to the web server by going to `http://192.168.42.1`

### Running the scripts

1. `sudo bash ap.sh`
2. `sudo python3 server.py`

Note that `sudo` is required for both scripts.

..
