# Raspberry Pi Picoを用いたフォトリフレクタのテストプログラム
from machine import ADC, Pin
from time import sleep

photorefL = Pin(26, Pin.IN)
photorefR = Pin(27, Pin.IN)

while True:
    print(photorefL.value(), photorefR.value())
    sleep(0.1)
