# Engineering_F.e.R.a

Able to test parts in the lab, and identify parts using A.I. recognition
<br>
<br>

## Table of Contents
* [Project F.e.](#parts-tester)
   * [Problems and Solutions](#problems-and-solutions)
   * [Description](#description)
   * [Code](#coding)
   * [Images](#images-progress)
   * [Links](#related-links)


<br>
<br>

## Budget

<br>
$100

   * $50 = party upon completion of Project F.e.
   * $50 = party upon completion of Project R.a.
<br>
<br>
<br>


## Schedule
<br>
<br>

Parts Tester: Achievement   |   Date  |
------------- |-------- |
Research | Week 1 |
Begin Code And Wiring | Week 2 - 6 |
Begin CAD And Manufacturing | Week 2 - 6 |
Begin Assembly and Testing | Week 7 - 9 |
Final Testing | Week 10 |
Small Iterations | Week 11 |
Documentation | Week 1-11 |

<br>
<br>

AI Recognition: Achievement   |   Date  |
------------- |-------- |
Research | Week 12 |
Begin Code And Wiring | Week 13 - 17 |
Begin CAD And Manufacturing | Week 13 - 17 |
Begin Assembly and Testing | Week 18 - 20 |
Final Testing | Week 21 |
Small Iterations | Week 22 |
Documentation | Week 1-22 |



<br>
<br>
<br>

## Iteration

<br>
<br>

<details>
<summary>Test Box</summary>
  
   * The Pseudocode for the Test Box
<br>

```mermaid
flowchart TD
    A(((Human Input))) -->B(Check for plugged in devices)
    B --> C{Device Outputs}
    E[Servos]
    D[Toggle 0-90]
    F[LCD]
    G[Draws text]
    H[Ultrasonic sensor]
    J[LED]
    K[Blinks]
    L[Photocell]
    N[RGB LED] 
    O[OLED]
    P[Photointerrupter]
    subgraph Devices
    direction TB
    subgraph  
    
    subgraph Servos
    direction RL
    E-->D
    end
    L
    P
    H
    end
    subgraph Screens
    direction TB
    F---O
    F-->G
    O-->G
    end
    H-->Screens
    subgraph LEDs
    direction TB
    subgraph  
    direction RL
    J---N
    end
    J-->K
    N-->K
    end

end
C-->Devices
L-->LEDs
P-->LEDs
```

<br>


  *Circuit Diagram of Test Box

![Test Box Circuit Diagram](Images/FECircuit.png)

<br>

   * The requirements of the Test Box.
<br>

![for Test Box essential and non...](Images/Essential%20and%20Nonessential%20for%20Capstone%20[Test%20Box].jpg)

<br>
<br>

   * The views from different sides of the box. 
<br>

![for AI essential and non...](Images/Views%20and%20parts%20of%20the%20Project.jpg)

<br>
<br>

</details>
<br>
<br>

   * The requirements of the AI.
<br>

![for AI essential and non...](Images/Essential%20and%20Nonessential%20for%20Capstone%20[AI].jpg)

<br>



<br>
<br>



  * The Psuedocode for the AI.
<br>

```mermaid
flowchart TD
    A[Device Starts] -->|Button?| B[/Takes Camera input/]
    B --> C[(Compare to reference images)]
    C --> D{Predict part identity}
    D --> E[Take part prediction]
    E --> F[run part prediction through bin table]
    F --> G[/display table with highlighted box/]
```
    
<br>
<br>
<br>

</details>

<br>
<br>

## Parts Tester

<br>
<br>
<br>

### Description
A box that quickly tests certain types of parts

<br>
<br>

### Problems and Solutions

* **Problem:** We didn't remember most of the code, and syntax which made it harder to code the assignment
   
   * **Solution:** Googled different things that would be used in the code so that it could be integrated to work with one another.
 
* **Problem:** The LCD Screen consists of multiple addresses, so knowing which address goes to which LCD Screen, and how the code would integrate all of them created an obstacle.
   
   * **Solution:** Used the most popular addresses and added them to a list that the code can use to reference if an LCD Screen in the lab has it. This would allow a wider array of LCDs to be tested.

* **Problem:** The OLED Code broke the LCD screen's code by adding corrupted text on the display.
   
   * **Solution:** This ended up being an address conflict error when the OLED code found the existence of an address on the LCD. Because it did not understand how to do those things, it created the glitchy text. Just checking typical addresses first solved this problem... for now.
 
* **Problem:** A rail was soldered on the circuit board at an angle.
   
   * **Solution:** Give it a little more space on the cut for the prototype.
     
* **Problem:** A combination of senioritis and Tardies delayed the project.
  
   * **Solution:** Work harder when we are there.
 
* **Problem:** Struggle to decide whether to keep the Photo-interrupter because of the difficulty in preventing short circuits and integrating it into the Box.

   * **Solution:** Remove the part to stay on schedule, and decide whether to add it later.

* **Problem:** Having the **servo,** **RGB LED,** **LED,** and **Photo-resister** separate, and having printed brackets to each, along with their small size is inconvenient and inefficient

   * **Solution:** Have those **four parts** on a small circuit board, and then attach the circuit board to the **Box**.
     
* **Problem** Soldering wires to floating headers is PAINFUL.

  * **Solution** Just get it over with and leave it to others (if you want to modify it, this should probably be changed).
    
* **Problem** OLED would not connect

  * **Solution** I accidentally forgot to put an **else** statement for when the other i2c device is in, such that it only ran one at a time, despite the capacity for more.
 

<br>
<br>

### Coding
This is the proof of concept code (to make sure that all of the devics could function simultaneously), and the Final code, which has the logic built into it.

<br>

<details>
<summary>Proof of concept code</summary>

```python
```circuitpython

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
```

</details>

<br>
<br>
<br>

<details>
<summary>Final code</summary>
  
```python
```circuitpython

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
#Photointerrupter
interrupter = digitalio.DigitalInOut(board.GP10)
interrupter.direction = digitalio.Direction.INPUT
interrupter.pull = digitalio.Pull.UP
#photointerrupter intended LED
interLed = digitalio.DigitalInOut(board.GP11)
interLed.direction = digitalio.Direction.OUTPUT
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
oaddr=0
i2c=False#has an I2C ever been plugged during this run
inv=False#this is the toggle check for OLED (screen should change black/white)
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
                except:
                    pass
            try:#try to set up OLED output
                oled.fill(0)
                oled.show()
                altscreen=True
            except:
                pass
    if time.monotonic()>=altTime+.25:#runs every 1/4 seconds
        altTime=time.monotonic()
        try:
            oled.invert(inv)
            inv = not inv
        except:#if OLED is gone there is none
            altscreen=False
            addrList.append(oaddr)
            oaddr=0
    if (time.monotonic()>=ledTime+1):#lights every 1 second
        ledTime=time.monotonic()
        if (ledState==True):#blinks LED
            ledState=False
            led.value=False
        elif (ledState==False):
            ledState=True
            led.value=True
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
        if (photocell.value>500):#if it is "dark"(may vary between photocells)-warrants checkback ***maybe switch
            cellLed.value=True
        else:
            cellLed.value=False#if normal or unplugged LED lights up
        if interrupter.value==False:#if light is blocked
            interLed.value=True
        else:
            interLed.value=False
            #extra
        
```

</details>
<br>
<br>

### Images progress

<br>
<br>

<details>
<summary>CLICK ME</summary>

<br>
<br>

<details>
<summary>CAD Walls</summary>

Onshape-designed **walls**.

<br>
<br>

* The **Back** side of the Test Box.

<br>

<img src="Images/Back. - Side..PNG" alt="the Back wall of the box" width="550" height="450">

<br>
<br>

* The **Bottom Base** of the Test Box.

<br>

<img src="Images/Bottom Base.PNG" alt="the Bottom Base of the box" width="600" height="450">

<br>
<br>

* The **Front** Side of the Test Box.

<img src="Images/Front. - Side.PNG" alt="the Front wall of the box" width="550" height="200">

<br>
<br>

* The **Inner** Side of the Test Box.

<img src="Images/Inner. - Side..PNG" alt="the Inner-Side wall of the box" width="550" height="270">

<br>
<br>

* The **Left** Side of the Test Box.

<img src="Images/Left Side.PNG" alt="the Left wall of the box" width="550" height="310">

<br>
<br>

* The **Right** Wall of the Test Box.

<img src="Images/Right Side.PNG" alt="the Right wall of the box" width="550" height="305">

<br>
<br>

* The **Top Cliff-Wall** of the Test Box.

<img src="Images/Top Cliff Wall.PNG" alt="the Top-CLiff-wall of the box" width="550" height="270">

<br>
<br>

* The **Upper Base** of the Test Box.

<img src="Images/Upper Base.PNG" alt="the Upper Base of the box" width="550" height="500">

</details>

<br>
<br>

---

<br>
<br>

<details>
<summary>Dupont Connector Brackets</summary>

CAD-designed brackets for the Dupont connectors 

<br>
<br>

* Dupont Connector for the **LCD**.

<br>

<img src="Images/Dupont Connector (LCD).PNG" alt="the Upper Base of the box" width="550" height="500">

<br>
<br>

* Dupont Connector for the **OLED**.

<img src="Images/Dupont Connector (OLED).PNG" alt="the Upper Base of the box" width="550" height="500">


</details>

<br>
<br>
<br>

* Assembly of the **Test Box**

<img src="Images/F.e.R.a. - Assembly (Top view).jpg" alt="the Test Box from top" width="550" height="650">

<img src="Images/F.e.R.a. - Assembly (Topographic).jpg" alt="the Test Box from an angle" width="550" height="550">

<br>
<br>

</details>

<br>
<br>
<br>

### Related Links


<br>
<br>


