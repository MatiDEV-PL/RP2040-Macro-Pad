import time
import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Initialize LED
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

# Define pin mappings
pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
]

# Define constants for key types
MEDIA = 1
KEY = 2

# Define key mappings
keymap = {
    0: (KEY, [Keycode.F8]),  # "Discord mute" "F8"
    1: (KEY, [Keycode.DELETE]),  # "BRUH" "Delete"
    2: (KEY, [Keycode.KEYPAD_PLUS]),  # "Increase volume" "🠕" "Made possible using Hotkeys"
    3: (KEY, [Keycode.WINDOWS, Keycode.SHIFT, Keycode.S]),  # "Snipping tool" "Print"
    4: (KEY, [Keycode.KEYPAD_ZERO]),  # "Mute" "/" "Made possible using Hotkeys"
    5: (KEY, [Keycode.KEYPAD_MINUS]),  # "Reduce volume" "🠗" "Made possible using Hotkeys"
    6: (KEY, [Keycode.CONTROL, Keycode.L]),  # "Opens folder" "F1"
    7: (KEY, [Keycode.PAUSE]),  # "Mute Microphone" "PAUSE/BRAKE" "Made possible using Hotkeys"
    8: (KEY, [Keycode.F3]),  # "F3" "F3"
}

# Initialize switch inputs
switches = []
switch_state = [False] * 9

for pin in pins:
    switch = DigitalInOut(pin)
    switch.direction = Direction.INPUT
    switch.pull = Pull.UP
    switches.append(switch)

# Initialize keyboard and consumer control objects
kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

# Main loop
while True:
    for button, switch in enumerate(switches):
        if not switch_state[button]:
            if not switch.value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.press(*keymap[button][1])  # Press the defined key(s)
                    else:
                        cc.send(keymap[button][1])  # Send the defined consumer control code(s)
                except ValueError:
                    pass  # Ignore any errors

                switch_state[button] = True  # Set switch state as active

        if switch_state[button]:
            if switch.value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.release(*keymap[button][1])  # Release the defined key(s)
                except ValueError:
                    pass  # Ignore any errors

                switch_state[button] = False  # Set switch state as inactive

    time.sleep(0.05)  # Pause before the next iteration
