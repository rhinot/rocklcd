import I2C_LCD_driver
import linecache
import random
import threading
import os
# import keyboard
from time import *

# Initialize the LCD screen
mylcd = I2C_LCD_driver.lcd()

################################################
# Get string - either manual entry or from a file
#text_string = "Hello World!"

# Pick specific line that is day of year
# day_of_year = strftime("%j") 
# text_string = day_of_year + " " + linecache.getline("quotes.txt",day_of_year)

# Random line selection
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
text_string = random_line("quotes.txt")
author_start = str.find(text_string,"-")
quote = text_string[0:author_start-1]
author = text_string[author_start:len(text_string)]
################################################

# Display author on LCD line 2
lcd2_string = author

# Loop quote on LCD line 1
str_pad = " " * 16
lcd1_string = str_pad + quote

###############################################
# Control LCD screens
#  
# LCD screen row 1 (left to right)
def LCD_row1(lcd1_string, stop):
	while True:
		for i in range (0, len(lcd1_string)):
			lcd1_text = lcd1_string[i:(i+16)]
			mylcd.lcd_display_string(lcd1_text,1)
			sleep(0.1)
			mylcd.lcd_display_string(str_pad,1)
			if stop:
				break

"""
# Commenting out until I can figure out how to control two lines of an LCD with threading without overloading the driver
# LCD screen row 2 (oscillate)
def LCD_row2(lcd2_string, stop):
	if (len(lcd2_string) < 17):
		mylcd.lcd_display_string(lcd2_string,2)
	else:
		while True:
			for i in range (0, len(lcd2_string)-16):
				lcd2_text = lcd2_string[i:(i+16)]
				mylcd.lcd_display_string(lcd2_text,2)
				sleep(0.5)
				mylcd.lcd_display_string(str_pad,2)
			for i in range (len(lcd2_string)-16, 0, -1):
				lcd2_text = lcd2_string[i:(i+16)]
				mylcd.lcd_display_string(lcd2_text,2)
				sleep(0.5)
				mylcd.lcd_display_string(str_pad,2)
			if stop:
				break
#################################################

# Thread the screen rows
stop_threads = False

thread1 = threading.Thread(target=LCD_row1,args=(lcd1_string, stop_threads,))
thread1.start()

thread2 = threading.Thread(target=LCD_row2,args=(lcd2_string, stop_threads,))
thread2.start()

# while keyboard.wait('esc'):
#	stop_threads = true
#	thread1.join()
#	thread2.join()
"""

# LCD_row2(lcd2_string, False)
mylcd.lcd_display_string(lcd2_string,2)
LCD_row1(lcd1_string, False)
