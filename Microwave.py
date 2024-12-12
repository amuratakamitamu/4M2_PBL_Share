from machine import Pin
from utime import sleep, ticks_us

trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)


def ultrasonic_sensor():
    # Read ultrasonic sensor
    trigger.value(0)
    sleep(0.000002)
    trigger.value(1)
    sleep(0.00001)
    trigger.value(0)

    pulse_start = pulse_end = 0
    while echo.value() == 0:
        pulse_start = ticks_us()

    while echo.value() == 1:
        pulse_end = ticks_us()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 0.0343 / 2
    return distance


while True:
    distance = ultrasonic_sensor()
    print(distance)
    sleep(0.2)
