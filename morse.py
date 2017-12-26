#short = 0.2
#long = 0.6
import time
import RPi.GPIO as GPIO

def dash():
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.2)

def dot():
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.2)

def space():
    time.sleep(1)

def letterSleep():
    time.sleep(0.6)

def a():
    letterSleep()
    dot()
    dash()

def b():
    letterSleep()
    dash()
    dot()
    dot()
    dot()

def c():
    letterSleep()
    for i in range(0,2):
        dash()
        dot()

def d():
    letterSleep()
    dash()
    dot()
    dot()

def e():
    letterSleep()
    dot()

def f():
    letterSleep()
    dot()
    dot()
    dash()
    dot()

def g():
    letterSleep()
    dash()
    dash()
    dot()

def h():
    letterSleep()
    for i in range(0,4):
        dot()

def i(): 
    letterSleep()
    dot()
    dot()

def j():
    letterSleep()
    dot()
    for i in range(0,3):
        dash()

def k():
    letterSleep()
    dash()
    dot()
    dash()

def l():
    letterSleep()
    dot()
    dash()
    dot()
    dot()

def m():
    letterSleep()
    dash()
    dash()

def n():
    letterSleep()
    dash()
    dot()

def o():
    letterSleep()
    for i in range(0,3):
        dash() 

def p():
    letterSleep()
    dot()
    dash()
    dash()
    dot()

def q():
    letterSleep()
    dash()
    dash()
    dot()
    dash()

def r():
    letterSleep()
    dot()
    dash()
    dot()

def s():
    letterSleep()
    for i in range(0,3):
       dot()

def t():
    letterSleep()
    dash()

def u():
    letterSleep()
    dot()
    dot()
    dash()

def v():
    letterSleep()
    for i in range(0,3):
        dot()
    dash()

def w():
    letterSleep()
    dot()
    dash()
    dash()

def x():
    letterSleep()
    dash()
    dot()
    dot()
    dash()

def y():
    letterSleep()
    dash()
    dot()
    dash()
    dash()

def z(): 
    letterSleep()
    dash()
    dash()
    dot()
    dot()





