#Need to add RGB LCD OLED
#type:ignore
#Requires the imports of The following files* to Libraries
#*Or folders
#*adafruit_bus_device
#*adafruit_motor
#you need to create a folder named lcd with the __init__ i2c_pcf8574_interface and lcd
#adafruit_framebuf
#adafruit_hcsr04
#adafruit_ssd1306
#rgb.py located on the Github repo
import board
import busio#I2C
import digitalio#most boolean type outputs LED/Photointerrupter
import adafruit_ssd1306#OLED?
import pwmio#servos amd stuff
import time#time.monotonic
from lcd.lcd import LCD#LCD 
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface#also LCD
import analogio#photocell/numerical returns
import adafruit_hcsr04#ultrasonic sensor
from adafruit_motor import servo#servos
from rgb import RGB#RGB LED
import random
from adafruit_display_text import label
print("sdfgh")#are we sure that this is actually running??
#Section for devices that might as well always be loaded because them existing won't crash it and it will work as soon as plugged in
#Pins also won't change anyway
#We used pins 1,2,7,8,9,10,11,13,14,15,26
#OLED reset pin
reset_pin = digitalio.DigitalInOut(board.GP1)
#LED initialization
led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT
#RGB initialization
r = board.GP7
g = board.GP8
b = board.GP9
myRGBled = RGB(r, g, b)
#Servo initialization
pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
#Photocell
photocell = analogio.AnalogIn(board.GP26)
cellLed = digitalio.DigitalInOut(board.GP2)
cellLed.direction = digitalio.Direction.OUTPUT
#Ultrasonic Sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP17, echo_pin=board.GP16)
#Tracks Time.monotonic's last runtime for each device
ledTime=time.monotonic()#all lighting not integrated in the box here
ledState=False#blinks LED
rgbState=0 #switches between 0(red),1(green), and 2(blue)
altTime=time.monotonic()
altscreen=False#OLED reference
servoTime=time.monotonic()
servoState=0#servo angle
screen=False#is there currently an LCD to display on
ultraDelay=time.monotonic()  #This is for the Ultrasonic sensor
result=0#records last result of ultrasonic sensor
#Photointerrupter does not need a time
#This is a list of EVERY SINGLE i2c address. Going to add a for stetment to check for addresses
addrList=[0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x0c,0x0d,0x0e,0x0f,
0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x1a,0x1b,0x1c,0x1d,0x1e,0x1f,
0x20,0x21,0x22,0x23,0x24,0x25,0x26,0x27,0x28,0x29,0x2a,0x2b,0x2c,0x2d,0x2e,0x2f,
0x30,0x31,0x33,0x36,0x38,0x39,0x3a,0x3b,0x3c,0x3d,0x3e,0x3f,
0x40,0x41,0x42,0x43,0x44,0x45,0x46,0x47,0x48,0x49,0x4a,0x4b,0x4c,0x4d,0x4e,0x4f,
0x50,0x51,0x52,0x53,0x54,0x55,0x56,0x57,0x58,0x59,0x5a,0x5b,0x5c,0x5d,0x5e,0x5f,
0x60,0x61,0x62,0x63,0x64,0x65,0x66,0x67,0x68,0x69,0x6a,0x6b,0x6c,0x6d,0x6e,0x6f,
0x70,0x71,0x72,0x73,0x74,0x75,0x76,0x77,0x78,0x79,0x7a,0x7b,0x7c,0x7d,0x7e,0x7f]
laddr=0
n=0
oaddr=0
x=0#x position of random pixel
y=0#y position of random pixel
i2c=False#has an I2C ever been plugged during this run
while True:
    if i2c==False or screen==False or altscreen==False:#area to check for any I2C device as well as either screen type(it breaks if it is attempted to be loaded when not plugged in)
        if i2c==False:#do we have I2C set yet?
            try:
                i2c_bus_0 = busio.I2C(board.GP15, board.GP14)
                i2c=True
            except RuntimeError:#luckily this can ONLY runtime error(2 types of errors do not work well for nice excepts)
                i2c=False
        if i2c==True and screen==False:#Do we have an I2C but no screen
            for i in addrList:
                try:#check most common LCD address
                    interface = I2CPCF8574Interface(i2c_bus_0, i)
                    lcd = LCD(interface, num_rows=2, num_cols=16)
                    screen=True
                    lcd.print("START")
                    print("LCD")
                    laddr=i
                    addrList.remove(i)
                except:
                    pass
        if i2c==True and altscreen==False:#do we have an OLED right now?
            for x in addrList:
                try:#check most common OLED address
                    oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c_bus_0, addr=x)
                    oaddr = x
                    addrList.remove(x)
                    print("up")
                    altscreen=True
                    break
                except:
                    pass
            if altscreen==True:#try to set up OLED output
                oled.fill(0)
                oled.show()
    if time.monotonic()>=altTime+.25:#runs every 1/4 seconds
        altTime=time.monotonic()
        if altscreen == True:
            try:
                x=random.randrange(0,128)
                y=random.randrange(0,64)
                oled.pixel(x,y,1)
                n+=1
                if n>=50:
                    n=0
                    oled.fill(0)
                oled.show()
            except:#if OLED is gone there is none
                altscreen=False
                addrList.append(oaddr)
                oaddr=0
    if (time.monotonic()>=ledTime+1):#lights every 1 second
        ledTime=time.monotonic()
        ledState=not ledState
        led.value=ledState
        if rgbState == 0:#modifies RGB LED coloration
            rgbState+=1
            myRGBled.red()
        elif rgbState == 1:
            rgbState+=1
            myRGBled.green()#green looks very pink... If you want to fix this, feel free, just wasn't really worth time
        else:
            rgbState=0
            myRGBled.blue()
    if (time.monotonic()>=servoTime+5):#servo swings every 5 seconds
        servoTime=time.monotonic()
        if servoState==0:#switch 0/90 degrees, safe pick for any type of servo
            servoState=90
        elif servoState==90:
            servoState=0
        servo1.angle=servoState
    if (time.monotonic()>=ultraDelay+.5):#ultrasonic sensro pings every 1/5 seconds
        ultraDelay=time.monotonic()
        try:#ultrasonic will break if it does not get a return ping, most ultrasonic sensor codes in this language have a try
            result=str(sonar.distance)
            if (screen==True):#do we have a screen?
                try:
                    lcd.clear()
                    lcd.print(result)
                except:
                    screen=False
                    addrList.append(laddr)
                    laddr=0
            else:#else use serial monitor
                print(result)
        except RuntimeError:#no return ping (either not plugged in or bounced at a bad angle)
            if (screen==True):
                try:
                    lcd.clear()
                    lcd.print("Testing")
                except:
                    screen=False
                    addrList.append(laddr)
                    laddr=0
            else:#I got complaints about it printing to the serial monitor and wanted to be petty instead of writing something for a very impractical scenario because serial monitor is for bug fixing anyway
                pass
    #will run every instance ~20 times a second, I never counted, but it loops pretty quickly
    if (photocell.value>1000 or photocell.value<400):#if it is "dark"(may vary between photocells)-warrants checkback ***maybe switch
        cellLed.value=True
    else:
        cellLed.value=False#if normal or unplugged LED lights up
        print(photocell.value)
