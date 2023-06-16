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
            os.system("sudo bash ./run_wifi.sh")
        # Add a small delay to debounce the button
        time.sleep(0.3)
except KeyboardInterrupt:
    GPIO.cleanup()
