"""
LCD python module for Raspberry Pi
Copyright (c) 2019-2020 Minh-An Dao for Maker Innovation Space, Can Tho University
All rights reserved.

"""
from lcd.LCD_I2C import LCD_I2C

# -----Address and Screen parameter:
LCD_ADDRESS = 0x27
LCD_WIDTH = 20
LCD_HEIGHT = 4

# ----- Initialize LCD
LCD = LCD_I2C(LCD_ADDRESS, LCD_WIDTH, LCD_HEIGHT)
LCD.clear()

__version__ = '1.0'
