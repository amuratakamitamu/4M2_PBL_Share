# Raspberry Pi Picoを用いたフォトリフレクタのテストプログラム
from machine import Pin, ADC
from time import sleep

photorefL = ADC(Pin(26))
photorefR = ADC(Pin(27))

error_sum = 0
count = 0

while True:
    photoref_outR = photorefR.read_u16()
    photoref_outL = photorefL.read_u16()
    error = photoref_outR - photoref_outL
    error_sum += error
    count += 1
    average_error = error_sum / count
    print(photoref_outL, photoref_outR, "error=",
          error, "average_error=", average_error)
    sleep(0.1)
