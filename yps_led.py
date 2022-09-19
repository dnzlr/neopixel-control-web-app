# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
from rpi_ws281x import *

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
LED_ORDER = neopixel.GRB
# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
#pixels = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, pixel_order=LED_ORDER)

# Intialize the library (must be called once before other functions).
#strip.begin()
def initLED():
    pixels = neopixel.NeoPixel(pixel_pin, LED_COUNT, brightness=1.0, auto_write=False, pixel_order=LED_ORDER)
    return pixels

ledObject = initLED()

WHITE = (255, 255, 255)
WARMWHITE = (255, 197, 142)
YELLOW = (250, 250, 51)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (240, 248, 255)
ORANGE = (255, 136, 0)
PINK = (255,20,147)
OFF = (0, 0, 0)


def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(LED_COUNT):
        strip[i] = (0,0,0)
        strip.write()

def cyclone(np):
    # cycle
    for i in range(4*LED_COUNT):
        for j in range(LED_COUNT):
            np[j] = (0, 0, 0)
        np[i % LED_COUNT] = (255, 255, 255)
        np.write()
        time.sleep(0.25)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)

        if LED_ORDER in (neopixel.RGB, neopixel.GRB):
            return (r, g, b)

        else:
            (r, g, b, 0)

        # THIS LINE KEEPS THE WHEEL SPINNIN FO EVAA
        #return (r, g, b) if LED_ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def wheelOff():
    strip = neopixel.NeoPixel(pixel_pin, LED_COUNT, brightness=0.0, auto_write=False, pixel_order=LED_ORDER)
    for i in range(LED_COUNT):
        strip[i] = (0,0,0)
        strip.write()
    strip.fill(OFF)
    strip.show()
    time.sleep(1)
        #print(str(isAlive))
        #print("JETZT ABER")
        #return (r, g, b, 0)


#def rainbow_cycle(wait):
#    for j in range(255*5):
#        for i in range(LED_COUNT):
#            pixel_index = (i * 256 // LED_COUNT) + j
#            pixels[i] = wheel(pixel_index & 255)
#            pixels.show()
#    #time.sleep(20/1000)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    for j in range(256*iterations):
        for i in range(LED_COUNT):
            pixel_index = (i * 256 // LED_COUNT) + j
            strip[i] = wheel(pixel_index & 255)
        strip.show()
        time.sleep(wait_ms/1000.0)

# rewrite this to color class

def ypsCol(pixels,rgb, brightah=1.0):
    pixels.fill(rgb)
    pixels.show()


#def ypsAllWhite_50():
#    pixels.fill(((int(255*0.5), int(255*0.5), int(255*0.5)))
#    pixels.show()

#while True:
    # Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    #pixels.show()
    #time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
    #pixels.show()
    #time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    #pixels.show()
    #time.sleep(1)

    #rainbow_cycle(0.011)  # rainbow cycle with 1ms delay per step
    #rainbow_cycle_yps()  # rainbow cycle with 1ms delay per step
    #ypsAllYellow()
    #ypsAllWarmWhite()
    #ypsAllWhite()
    #ypsAllRed()

