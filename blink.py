from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)
red = Pin(18, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)


print("LED starts flashing...")
while True:
    try:
        led.toggle()
        red.toggle()
        yellow.toggle()
        green.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
led.off()
red.off()
yellow.off()
green.off()
print("Finished.")
