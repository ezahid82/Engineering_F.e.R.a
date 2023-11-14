#type:ignore
import board
import busio
import digitalio
import adafruit_ssd1306
import pwmio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import analogio
from lcd.lcd import CursorMode
import adafruit_hcsr04
from adafruit_motor import servo
reset_pin = digitalio.DigitalInOut(board.GP10)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP17, echo_pin=board.GP16)
i2c_address = 0x27
cols = 16
rows = 2
i2c_bus_0 = busio.I2C(board.GP15, board.GP14) # 1 rn
interface = I2CPCF8574Interface(i2c_bus_0, i2c_address)
lcd = LCD(interface, num_rows=rows, num_cols=cols)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c_bus_0, addr=0x3d)
led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT
photocell = analogio.AnalogIn(board.GP26)
pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
ultra=0
cell=0
tog=1
per=0
# Start at the second line, fifth column (numbering from zero).
# Make the cursor visible as a line.
oled.fill(0)
oled.show()
#Ultrasonic problem
while True: 
    try:
        ultra=sonar.distance
        print(ultra)
        lcd.print(str(ultra))
    except RuntimeError:
        print("Retrying!")
        lcd.print("Retrying")
    cell=photocell.value
    if (cell<30000):
        led.value=True
    else:
        led.value=False
    if (per==10):
        per=0
        if (tog==1):
            servo1.angle=0
            oled.invert(True)
            tog=0
        elif (tog==0):
            servo1.angle=90
            oled.invert(False)
            tog=1
    time.sleep(0.2)
    per+=1
    lcd.clear()
