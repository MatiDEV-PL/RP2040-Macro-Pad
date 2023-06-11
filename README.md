# RP2040-Macro-Pad based on [Sebastian Proost Project](https://www.thingiverse.com/thing:4816077)
Whats neded:
* 1x a RP2040-Macro-Pad case (my printed with resolution 0.13 and infill 50% on Monoprice MP select mini V2)
* 1x a RP2040 (any variant of the board will fit)
* 9x Mechanical keyboard switches
* 9x keycaps of your choice
* 1x a switch opener (optional)
* 4x M3 bolts (1 cm long)
* wires
* soldering equipment
* a hot-glue gun
* a USB-micro/c cable

# RP2040-Macro-Pad GPIO Pinout
![Imgur](https://i.imgur.com/i9qHdCf.png)

# Steps:
* Get everything whats neded
* Get RP2040 in bootloader mode and install [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/)
* Solder the cables exactly as in the drawing above.
* Copy files from code folder to RP2040
* Attach the board to the case using hot-glue
* Close everything up with bolts.
* Done, now you can define your own key mappings in code.py. List of keycodes (keycode.py) and media controls (consumer_control_code.py) are located in lib\adafruit_hid
* Optional step if you are using windows you can remove RP2040 storage letter in computer management so it looks like it's regular macro-pad
