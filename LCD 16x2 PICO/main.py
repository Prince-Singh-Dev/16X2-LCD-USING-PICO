from machine import Pin
from gpio_lcd import GpioLcd

#Declaring pins 
lcd=GpioLcd(rs_pin=Pin(16),
                enable_pin=Pin(17),
                d4_pin=Pin(21),
                d5_pin=Pin(20),
                d6_pin=Pin(19),
                d7_pin=Pin(18),
                num_lines=2,
                num_columns=16)

button = Pin(0,Pin.IN,Pin.PULL_UP) #button function 

lcd.move_to(3,1) #to set the cursor on 2nd column and 1st row 
lcd.putstr("LALLAN :)") #to print anything on the LCD
if(button.value()==1): #to check value on button
  lcd.putstr(" TOP <..>") #Printing this on LCD

#CONNECTIONS WITH PICO OF LCD
#(VSS,V0,RW,K) --> GND
#(VDD,A) --> VBUS
#(RS,E) --> (16,17)
#(D4,D5,D6,D7) --> (21,20,19,18)

#CONNECTION OF PUSH BUTTON WITH PICO
#BUTTON'S (+VE , -VE) --> (0,GND)