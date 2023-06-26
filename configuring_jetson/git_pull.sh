#!/bin/bash

# the function to check the internet connection
function check_internet() {
    wget -q --spider https://google.com

    if [ $? -eq 0 ]; then
        return 0
    else
        return 1
    fi
}

# the function to pull the git repo
function git_pull() {
    cd /home/timf34/Desktop/FOVCamerasWebApp
    git pull
}

# check for internet connection once after boot
check_internet
while [ $? -ne 0 ]; do
    sleep 10
    check_internet
done

# Pull when device is initially connected to the internet
git_pull

# check for updates every 1 hour
while true; do
    check_internet
    if [ $? -eq 0 ]; then
        git_pull
    fi
    sleep 3600
done
