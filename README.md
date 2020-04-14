# LCD-I2C module for Raspberry Pi

## About
This is a Python module for the LCD display connected to a Raspberry Pi.

Designed for 20x4 (default), 16x2,... LCD (definitely not 12864 LCD).

Ported from C++ library for Arduino on [Github].


Ported by [Minh-An Dao], from Can Tho University, Vietnam.
Licensed under the MIT License. (c) 2019-2020

## Installation
 - Clone or download the repository to your Rasp.
 - Setup I2C before using:
    - Give permission to the setup file:
    ```bash
        chmod +x ./ setup-i2c
    ```
    - Run setup: _(only need to run once on a fresh Rasbian Buster installation)_
    ```bash
        sudo ./ setup-i2c
    ```
 - Run the demo:
```bash
python3 lcd.py
```
 - Now the LCD should show some letters. If not, please double check your wiring and the type of LCD.
 - You can change the number of rows and columns of the LCD in [initialization file] (default to be 20x4).
 - You can check inside the module to see what functions are available. Since I only port functions that are necessary for my project, you can not expect to have full functions as the original. However, I believe all basic functions for displaying the LCD are included.
 - Have fun coding!



<!-- Links -->
[Github]: https://github.com/fdebrabander/Arduino-LiquidCrystal-I2C-library
[Minh-An Dao]: https://bit.ly/DMA-HomePage
[initialization file]: /lcd/__init__.py