#type:ignore
import board
import adafruit_register
import adafruit_ssd1306
import digitalio
import busio
reset_pin = digitalio.DigitalInOut(board.GP10)
i2c = busio.I2C(board.GP15, board.GP14)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3d)


oled.fill(0)
oled.show()
while True:
    oled.invert(True)