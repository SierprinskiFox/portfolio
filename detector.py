# Code for the "detector" microbits. Make sure
# a speaker is attached in the usual way. a
from microbit import *
import radio
import music

radio.config(channel=10)
radio.on()

while True:
    message = radio.receive_full()
    if message:
        strength = message[1] + 100
        displaystrength = int((strength / 10) + 1)
        display.show(str(displaystrength))
        music.pitch(strength * 50, 100)
    else:
        display.show(Image.NO)

# Code for the "transmitter" microbits. a
from microbit imort *
import radio
id = "10"
display.show(id)
radio.config(power=0)
radio.config(channel=10)
radio.on()

while True:
    radio.send(id)