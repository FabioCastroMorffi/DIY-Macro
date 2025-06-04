import board
import displayio
import busio
import terminalio
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from adafruit_display_text import label
from adafruit_ssd1306 import SSD1306_I2C

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP0, board.GP1, board.GP2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#encoder
encoder = EncoderHandler()
encoder.encoder_pins = ((board.GP3, board.GP4),)  
encoder.rotate_callbacks = [
    lambda direction: keyboard.send(KC.VOLU if direction else KC.VOLD)
]
keyboard.modules.append(encoder)

#simple text display oled screen
displayio.release_displays()
i2c = busio.I2C(board.GP6, board.GP7)  

display = SSD1306_I2C(38, 12, i2c)
splash = displayio.Group()

text_area = label.Label(terminalio.FONT, text="DIY MACROPAD", x=2, y=10)
splash.append(text_area)
display.show(splash)



keyboard.keymap = [
    [
        KC.S, KC.I, KC.L,   
        KC.K, KC.S, KC.O,   
        KC.N, KC.G, KC.SPC,    
    ]
]

if __name__ == '__main__':
    while True:
        keyboard.go()


