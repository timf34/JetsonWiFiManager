Here's how you can set up this script. It's recommended to create a systemd service, as you suggest, which will handle the starting, stopping, and automatic restarting of the script should it ever fail.

Here are the steps:

1. Write your Python script as follows:

    ```python
    import Jetson.GPIO as GPIO
    import time
    import os

    # Set up GPIO mode and pin
    GPIO.setmode(GPIO.BOARD)
    button_pin = 37


    # Set up button pin as input
    GPIO.setup(button_pin, GPIO.IN)

    try:
        while True:
            
           #  Check if the button is pressed (active high)
            buttonState = GPIO.input(button_pin)
            if buttonState == False:
                os.system("sudo bash /path/to/run_wifi.sh")
            # Add a small delay to debounce the button
            time.sleep(0.3)
    except KeyboardInterrupt:
        GPIO.cleanup()
    ```

    This script will run the shell script when the button is pressed.

2. Save the script to a file, for example `button_press.py`. Make sure this file is executable:

    ```bash
    chmod +x /path/to/button_press.py
    ```

3. Create a new systemd service. Systemd is a system and service manager for Linux. It's used for initializing and managing many things, including user processes. Systemd also keeps track of all processes using the Linux cgroups mechanism, instead of using the conventional UNIX process hierarchy.

    Create a new file in `/etc/systemd/system/` called `button_press.service`:

    ```bash
    sudo nano /etc/systemd/system/button_press.service
    ```

    And paste the following:

    ```ini
    [Unit]
    Description=Run script on button press
    After=multi-user.target
    
    [Service]
    Type=idle
    ExecStart=/usr/bin/python3 button_press.py
    WorkingDirectory=/home/orin1/Desktop/JetsonWiFiManager/
    
    [Install]
    WantedBy=multi-user.target
    ```

    Save the file and exit.

4. Enable and start the service:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable button_press.service
    sudo systemctl start button_press.service
    ```

    With these commands, the script will run at startup, and it will be restarted if it ever crashes.

5. You can check the status of your service by running:

    ```bash
    sudo systemctl status button_press.service
    ```

    If you ever make changes to your Python script or the service file, be sure to restart the service:

    ```bash
    sudo systemctl restart button_press.service
    ```

A couple of things to note:

- When using `os.system`, remember that your Python script is running with the permissions of the user that started it (which in this case is root, because it's started by a system service). Therefore, it's important to ensure that your shell script (`run_wifi.sh`) does not have any security vulnerabilities, as it will also be run as root.

- The systemd service file assumes that your Python interpreter is located at `/usr/bin/python3`. If it is located elsewhere, you will need to update the `ExecStart` line with the correct path. You can check the location by running `which python3` in the terminal.