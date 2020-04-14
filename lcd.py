"""------------------------------------------------------------*-
  LCD example application for Raspberry Pi
  Tested on: Raspberry Pi 3 B+
  (c) Minh-An Dao 2019-2020
  version 1.10 - 14/04/2020
 --------------------------------------------------------------
 * Change rows and columns setting in lcd/__init__.py 
 * Default to be (20x4)
 *
 --------------------------------------------------------------"""
from lcd import LCD

# ------------------------------ LCD functions ------------------------------
def lcd_begin():
    LCD.backlight() # turn on backlight
    LCD.clear()
    LCD.setCursor(5, 0)  # row, column
    LCD.write("LCD ready!")
    LCD.setCursor(7, 2)  # row, column
    LCD.write("....")

# ---------------------------------------------------------------------------


if __name__ == '__main__':
    try:
        lcd_begin()
    except (KeyboardInterrupt, SystemExit, OSError, Exception) as e:
        print(e)
        