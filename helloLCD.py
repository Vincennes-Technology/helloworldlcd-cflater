#show IP address on the LCD Plate at startup
#
import subprocess
import time
import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()


IP = subprocess.check_output(['hostname','-I'])
Name = subprocess.check_output(['hostname']).strip()
displayText = Name

lcd.clear()

refresh = True

while(True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.set_backlight(1)
        lcd.message("HELLO WORLD\n")
        lcd.message(displayText)
        refresh = True
        time.sleep(0.5)

    else:
        if refresh:
            lcd.clear()
            lcd.set_backlight(1)
            lcd.message(IP)
            lcd.message(displayText)
            time.sleep(0.5)
            refresh = False





