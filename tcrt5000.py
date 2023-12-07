from machine import Pin, ADC, PWM
import time

TCRT_5000_Value = ADC(2)
TCRT_50002_Value = ADC(1)
led1 = Pin(11, Pin.OUT)
led2 = Pin(7, Pin.OUT)
servo = PWM(Pin(16))

servo.freq(50)

while True:
    print(TCRT_5000_Value.read_u16())
    
    if TCRT_5000_Value.read_u16() <=4000 or TCRT_50002_Value.read_u16() <=4000:
        led1.value(1)
        led2.value(0)
        pulsoY = 1500000
        servo.duty_ns(pulsoY)
        
    else:
        led1.value(0)
        led2.value(1)
        pulsoY = 2500000
        servo.duty_ns(pulsoY)
        
    time.sleep(0.01)
