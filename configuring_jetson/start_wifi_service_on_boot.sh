#!/bin/bash

# Unmask hostapd
sudo systemctl unmask hostapd

# define your script path
SCRIPT_PATH="/home/tim/Desktop/JetsonWiFiManager/run_wifi.sh" # replace with your script's actual path

# Make ap.sh executable
chmod +x $SCRIPT_PATH

# Create a systemd service
echo "[Unit]
Description=Start WiFi on boot
After=network.target

[Service]
ExecStart=/bin/bash $SCRIPT_PATH
WorkingDirectory=/home/tim/Desktop/JetsonWiFiManager
Environment=PYTHONPATH=/home/tim/.local/lib/python3.6/site-packages/flask
User=root
Type=oneshot
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/startwifi.service

# Reload systemd manager configuration
sudo systemctl daemon-reload

# Enable the service so it starts on boot
sudo systemctl enable startwifi

# Start the service
sudo systemctl start startwifi
