from machine import Pin, PWM
from time import sleep, ticks_us
import time
import rp2

duty_100 = 32768  # 100% duty cycle
v = int(duty_100//1.2)
time_tmp = time.time()

# Configure pins
M1A = PWM(Pin(5))  # Left motor forward
M1B = PWM(Pin(4))  # Left motor reverse
M2A = PWM(Pin(3))  # Right motor forward
M2B = PWM(Pin(2))  # Right motor reverse
photorefR = Pin(27, Pin.IN)  # Right photoreflector
photorefL = Pin(26, Pin.IN)  # Left photoreflector
trigger = Pin(14, Pin.OUT)  # Ultrasonic sensor trigger
echo = Pin(15, Pin.IN)  # Ultrasonic sensor echo

# Set PWM frequency
for motor in [M1A, M1B, M2A, M2B]:
    motor.freq(1000)

while True:
    if rp2.bootsel_button() == 1:
        break

try:
    while True:
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

        if distance <= 3.5:
            M1A.duty_u16(0)
            M2A.duty_u16(0)
            break
        elif photorefR.value() == 0:
            M1A.duty_u16(v)
            M2A.duty_u16(0)
        elif photorefL.value() == 0:
            M1A.duty_u16(0)
            M2A.duty_u16(v)
        else:
            M1A.duty_u16(v)
            M2A.duty_u16(v)

# Stop motor when Ctrl+C is pressed
except KeyboardInterrupt:
    for motor in [M1A, M1B, M2A, M2B]:
        motor.duty_u16(0)
