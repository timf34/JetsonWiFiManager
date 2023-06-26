#!/bin/bash

# Change ownership and permissions of the FOVCamerasWebApp Git repository
sudo chown -R timf34:timf34 /home/timf34/Desktop/FOVCamerasWebApp
sudo chmod -R 777 /home/timf34/Desktop/FOVCamerasWebApp

# Change ownership and permissions of the JetsonWiFiManager Git repository
sudo chown -R timf34:timf34 /home/timf34/Desktop/JetsonWiFiManager
sudo chmod -R 777 /home/timf34/Desktop/JetsonWiFiManager

# Make pull_git.sh executable
chmod +x /home/timf34/Desktop/JetsonWiFiManager/configuring_jetson/git_pull.sh

# Add the directory to the list of safe directories in Git's configuration
sudo git config --system --add safe.directory '*'

# Create a systemd service
echo "[Unit]
Description=Pull git on network connectivity
After=network.target

[Service]
ExecStart=/home/timf34/Desktop/JetsonWiFiManager/configuring_jetson/git_pull.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/gitpull.service

# Reload systemd manager configuration
sudo systemctl daemon-reload

# Enable the service
sudo systemctl enable gitpull

# Start the service
sudo systemctl start gitpull
