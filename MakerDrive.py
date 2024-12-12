# RaspberryPiPico, MakerDriveを用いたモータ制御のテストプログラム
# M1A: GPIO5, M1B: GPIO4, M2A: GPIO3, M2B: GPIO2

from machine import Pin, PWM
from time import sleep

duty_100 = 32768  # 100%デューティサイクル

# ピンの設定
M1A = PWM(Pin(5))
M1B = PWM(Pin(4))
M2A = PWM(Pin(3))
M2B = PWM(Pin(2))

# PWMの周波数を設定
M1A.freq(1000)
M1B.freq(1000)
M2A.freq(1000)
M2B.freq(1000)

# 前進
while True:
    M1A.duty_u16(duty_100//3)
    M1B.duty_u16(0)
    M2A.duty_u16(duty_100//3)
    M2B.duty_u16(0)
    sleep(2)
