# You import all the IOs of your board
import board
import os

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
#TODO This Pin layout corresponds to the labels provided by the KiCad library and seem a bit weird, so they might have to be updated in the final version
PINS = [board.D0, board.D27, board.D1, board.D7, board.D28, board.D2, board.D29, board.D4, board.D3]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [   KC.F6, KC.F7, KC.F8,
        KC.MACRO(Press(KC.LGUI), Tap(KC.KP_1), Release(KC.LGUI)),KC.MACRO(Press(KC.LGUI), Tap(KC.KP_2), Release(KC.LGUI)),KC.MACRO(Press(KC.LGUI), Tap(KC.KP_3), Release(KC.LGUI)),
        KC.MACRO(os.popen("kitty")), KC.Ins, KC.MACRO(os.system("flatpak run app.zen_browser.zen"))
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
