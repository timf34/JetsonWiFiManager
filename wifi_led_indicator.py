import Jetson.GPIO as GPIO
import time
import subprocess

# Set up GPIO mode and pin
GPIO.setmode(GPIO.BOARD)
LED_pin = 29

# Set up button pin as input
GPIO.setup(LED_pin, GPIO.OUT)
GPIO.output(LED_pin, GPIO.LOW)


def check_network_manager() -> bool:
    # Check if the network manager service is running
    try:
        subprocess.check_output(['systemctl', 'is-active', '--quiet', 'NetworkManager'])
        return True
    except subprocess.CalledProcessError:
        return False


def check_internet_connection() -> bool:
    # Check if the device is connected to the internet
    try:
        # Try to reach out to Google's primary DNS server to check for connectivity.
        subprocess.check_output(['ping', '-c', '1', '8.8.8.8'])
        print("connected to internet")
        return True
    except subprocess.CalledProcessError:
        print("not connected to internet")
        return False


def flash_LED() -> None:
    # LED should flash gently
    GPIO.output(LED_pin, GPIO.LOW)
    print("low")
    time.sleep(0.5)
    GPIO.output(LED_pin, GPIO.HIGH)
    print("high")
    time.sleep(0.5)
    GPIO.output(LED_pin, GPIO.LOW)


try:
    while True:
        if check_network_manager():
            if check_internet_connection():
                # Network Manager is on and connected to the internet, LED on
                GPIO.output(LED_pin, GPIO.HIGH)
            else:
                # Network Manager is on but not connected to the internet, LED off
                GPIO.output(LED_pin, GPIO.LOW)
        else:
            # Network Manager is off, LED should flash gently
            flash_LED()
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
