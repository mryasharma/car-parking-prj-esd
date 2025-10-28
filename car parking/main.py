from machine import Pin, PWM, I2C
from time import sleep, sleep_us
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# Constants for I2C LCD
I2C_ADDR = 0x27
I2C_ROWS = 2
I2C_COLS = 16

# Servo duty cycle constants
MIN_DUTY = 40
MAX_DUTY = 115

# Initialize I2C for LCD
i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_ROWS, I2C_COLS)

# Define servo control function
def set_servo_angle(servo, angle):
    duty = int(MIN_DUTY + (angle / 180) * (MAX_DUTY - MIN_DUTY))
    servo.duty(duty)

# Define pins for ultrasonic sensors and servo motor
trig_entry = Pin(15, Pin.OUT)  # Trigger pin for entry (HC-SR04)
echo_entry = Pin(2, Pin.IN)     # Echo pin for entry
trig_exit = Pin(4, Pin.OUT)     # Trigger pin for exit (HC-SR04)
echo_exit = Pin(5, Pin.IN)      # Echo pin for exit
servo = PWM(Pin(12), freq=50)   # Servo motor on pin 12

# Set initial position of servo to closed (0 degrees)
set_servo_angle(servo, 0)

# Parking system variables
max_slots = 4
current_occupied = 0

# Clear the LCD and print initial message
lcd.clear()
lcd.putstr("Car Parking Sys\nWaiting...")

# Function to measure distance using ultrasonic sensor
def measure_distance(trig, echo):
    trig.value(0)  # Ensure trigger is low
    sleep_us(2)
    trig.value(1)  # Set trigger high
    sleep_us(10)
    trig.value(0)  # Set trigger low

    pulse_start = 0
    pulse_end = 0

    # Wait for the echo pin to go high
    while echo.value() == 0:
        pulse_start += 1  # Increment pulse_start (simulated time in microseconds)

    # Wait for the echo pin to go low
    while echo.value() == 1:
        pulse_end += 1  # Increment pulse_end (simulated time in microseconds)

    pulse_duration = pulse_end - pulse_start  # Calculate pulse duration
    distance = (pulse_duration * 0.0343) / 2  # Convert duration to distance (cm)
    return distance

# Main loop
while True:
    # Check for entry
    distance_entry = measure_distance(trig_entry, echo_entry)
    if distance_entry < 2 and current_occupied < max_slots:  # Car detected within 2 cm for entry
        lcd.clear()
        lcd.putstr("Car at Entry\nOpening gate...")
        print("Car detected at entry. Opening gate...")
        set_servo_angle(servo, 90)  # Open gate
        sleep(2)
        lcd.clear()
        lcd.putstr("Gate Open\nPlease Enter")
        sleep(5)
        current_occupied += 1
        print(f"Car entered. Total parked: {current_occupied}")
        set_servo_angle(servo, 0)  # Close gate
        print("Gate closed.")
        lcd.clear()
        lcd.putstr("Gate Closed\nWaiting...")
        sleep(2)
        lcd.putstr(f"Parked: {current_occupied}/{max_slots}\nWaiting...")
        sleep(2)

    elif distance_entry < 2 and current_occupied >= max_slots:
        lcd.clear()
        lcd.putstr("Parking Full\nPlease Exit")
        print("Parking is full. Waiting for exit...")
        sleep(5)  # Show full message for 5 seconds

    # Check for exit
    distance_exit = measure_distance(trig_exit, echo_exit)
    if distance_exit < 2 and current_occupied > 0:  # Car detected within 2 cm for exit
        lcd.clear()
        lcd.putstr("Car at Exit\nOpening gate...")
        print("Car detected at exit. Opening gate...")
        set_servo_angle(servo, 90)  # Open gate
        sleep(2)
        lcd.clear()
        lcd.putstr("Gate Open\nPlease Exit")
        sleep(5)
        current_occupied -= 1
        print(f"Car exited. Total parked: {current_occupied}")
        set_servo_angle(servo, 0)  # Close gate
        print("Gate closed.")
        lcd.clear()
        lcd.putstr("Gate Closed\nWaiting...")
        sleep(2)
        lcd.putstr(f"Parked: {current_occupied}/{max_slots}\nWaiting...")
        sleep(2)

    elif distance_exit < 2 and current_occupied == 0:
        lcd.clear()
        lcd.putstr("No Cars to Exit\nWaiting...")
        print("No cars to exit. Waiting...")
        sleep(5)

    sleep(0.1)  # Short delay to avoid excessive processing
