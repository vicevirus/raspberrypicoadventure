from machine import Pin
import time
button = Pin(0, Pin.IN)

def buttonPress(num):
    global localState
    temp = num
    if (temp == 1) & (button.value() == 0):
        return 1
    elif (temp == 0) & (button.value() == 0):
        return 2
    elif (temp == 0) & (button.value() == 1):
        return 3
    else:
        return 0
lastState = 0
while True:

    lastState = button.value()
    print("                  " + str(button.value()))
    time.sleep_ms(50)
