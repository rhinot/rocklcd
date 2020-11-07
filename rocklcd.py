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
# Random line selection
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
text_string = random_line("quotes.txt")
author_start = str.find(text_string,"-")
quote = text_string[0:author_start-1]
author = text_string[author_start:len(text_string)]

################################################
# Code to store string in a list of 16 char strings
# Initialize variables
index = 0
pos = 0

# Intitialize list based on length of quote
lcd_seg = len(text_string)/16 + 3  # 1 for remander of quote, 1 for author, 1 for buffer
# If odd number of lines, add a blank line for ease of reading on a 2 line LCD
if (lcd_seg % 2 == 1):
	lcd_seg = lcd_seg + 1
lcd_str = [" "] * lcd_seg
print(text_string)
print(lcd_seg)

# Cut quote into 16 char segments
while pos < len(quote) - 1:
	# If search is out of bounds, set bound at end
	if (pos + 17 > len(quote)):
		lcd_str_spl = len(quote)
	else: 
		end_pos = pos + 17
		lcd_str_spl = quote.rfind(" ",pos,end_pos)
	lcd_str[index] = quote[pos:lcd_str_spl]
	print(lcd_str[index])
	print(len(lcd_str[index]))
	pos = lcd_str_spl + 1
	index = index + 1	

# Add author
lcd_str[index] = author
print(lcd_str[index])
print(len(lcd_str[index]))

###############################################
# Control LCD screen
#  
def LCD_row(lcd_str):
	while True:
		for i in range (0, len(lcd_str), 2):
			mylcd.lcd_clear()
			mylcd.lcd_display_string(lcd_str[i],1)
			mylcd.lcd_display_string(lcd_str[i+1],2)
			sleep(2)

#################################################

LCD_row(lcd_str)
