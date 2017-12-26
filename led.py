import RPi.GPIO as GPIO
import time
import morse


def flipLED(status):
    if status:
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
    


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
status = True

morse_map = {'a': morse.a, 'b': morse.b, 'c': morse.c, 'd': morse.d, 'e': morse.e, 
    'f': morse.f, 'g': morse.g, 'h': morse.h, 'i': morse.i, 'j': morse.j, 
    'k': morse.k, 'l': morse.l, 'm': morse.m, 'n': morse.n, 'o': morse.o, 
    'p': morse.p, 'q': morse.q, 'r': morse.r, 's': morse.s, 't': morse.t,
    'u': morse.u, 'v': morse.v, 'w': morse.w, 'x': morse.x, 'y': morse.y, 
    'z': morse.z, ' ': morse.space}

while True:
    temp = raw_input("Please enter a number (q to quit): ");
    num = -1
    try:
        num = int(temp)
    except:
        pass
        
    if temp == 'q':
        break

    if num > 0:
        i = 0
        while i < num * 2:
            flipLED(status)
            status = not status
            time.sleep(0.1)
            i += 1
    else: 
        for c in temp:
            morse_map[c]()
            time.sleep(0.1)
    
GPIO.output(18, GPIO.LOW)

