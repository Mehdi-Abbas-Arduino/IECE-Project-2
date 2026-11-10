from machine import Pin, time_pulse_us
from utime import sleep ,sleep_us 

ULTRA_PIN_Trigger = 2
ULTRA_PIN_Echo = 3
# VBUS = 40


ULTRA_PIN_Echo_pin = Pin(ULTRA_PIN_Echo,Pin.IN)
ULTRA_PIN_Trigger_pin = Pin(ULTRA_PIN_Trigger,Pin.OUT)

def func():
    ULTRA_PIN_Trigger_pin.low()
    sleep_us(2)
    ULTRA_PIN_Trigger_pin.high()
    sleep_us(10)
    ULTRA_PIN_Trigger_pin.low()
    t = time_pulse_us(ULTRA_PIN_Echo_pin,1,30000)
    if t < 0:
        return None
    return (t*0.03430) / 2


while True:
    d = func()
    print("No Echo" if d is None else f"Distance{d}")
    sleep(0.5)