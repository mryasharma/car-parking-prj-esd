🚗 Car Parking System using Ultrasonic Sensor, Servo Motor & LCD
📘 Project Overview

The Car Parking System is an embedded system project designed to automate the vehicle parking process using an ultrasonic sensor, servo motor, and LCD display.
It detects the presence of a car using distance measurement and automatically opens or closes the gate with a servo motor, while displaying real-time parking status on the LCD.

⚙️ Components Used

ESP32 / Arduino Uno (Microcontroller)

Ultrasonic Sensor (HC-SR04) – Detects car distance

Servo Motor (SG90) – Opens and closes the gate

16x2 LCD Display – Shows parking slot status

Buzzer (optional) – Alerts when a car enters or leaves

Jumper Wires and Breadboard – For connections

Power Supply (5V)

🧠 Working Principle

The ultrasonic sensor continuously measures distance.

When a car approaches within a certain range (e.g., < 10 cm),

The servo motor rotates to open the gate.

The LCD displays “Car Detected – Gate Opening”.

After a few seconds, once the car passes,

The servo motor returns to the closed position.

The LCD updates to “Slot Occupied” or “Gate Closed”.

This helps automate entry/exit and manage parking efficiently.

🧩 Features

Automatic gate control using sensor detection

Real-time LCD status updates

Compact and cost-effective system

Can be extended for multiple parking slots or IoT monitoring

🧠 Future Improvements

Add multiple ultrasonic sensors for multi-slot parking detection

Connect to a mobile app or web dashboard using Wi-Fi (ESP32)

Include IR sensors for more accurate detection

Integrate payment or booking features

Demo
<img width="1919" height="859" alt="image" src="https://github.com/user-attachments/assets/9c695894-2445-4743-ad60-ad82a77881d5" />
