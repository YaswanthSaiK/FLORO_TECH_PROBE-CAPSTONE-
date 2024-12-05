import RPi.GPIO as GPIO
import time

# Define the GPIO pin connected to the IR sensor
IR_PIN = 17

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)

try:
    while True:
        # Read the state of the IR sensor
        hand_detected = GPIO.input(IR_PIN)

        if hand_detected:
            print("Hand detected!")
        else:
            print("No hand detected.")

        # Add a small delay to avoid continuous detection
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program terminated by the user.")
finally:
    # Clean up GPIO on exit
    GPIO.cleanup()
