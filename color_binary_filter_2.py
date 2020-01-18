# Base off of Color Binary Filter Example
#
# This script shows off the binary image filter. You may pass binary any
# number of thresholds to segment the image by.

import sensor, image, time, pyb
from pyb import *

sensor.reset()
sensor.set_framesize(sensor.QQVGA)
sensor.set_pixformat(sensor.RGB565)
sensor.skip_frames(time = 2000)
clock = time.clock()

redled = pyb.LED(1)
grnled = pyb.LED(2)

torled = 0
togled = 0

allbits = 0

i2c = I2C(2)                         # create on bus 2
i2c.init(I2C.SLAVE, addr=0x3A)       # init as a slave with given address

# Use the Tools -> Machine Vision -> Threshold Edtor to pick better thresholds.
red_threshold = (0, 100, -128, 7, 35, 127) # L A B threshold

while(True):

    # Test red threshold
    clock.tick()
    img = sensor.snapshot()
    img.binary([red_threshold]) #Threshold it

    img.erode(5,4) #Remove noise
    img.dilate(2,2) #Fill in logo
    img.erode(2,2) #Account for dilation

    cwmax = 0
    blobs = img.find_blobs([(100,255),(100,255),(100,255)])
    aspect_ratio_ok = blobs[:]
    for i in range(0,len(blobs)):
        if(abs(blobs[i].w()-blobs[i].h()) > (blobs[i].w()/4)): #Aspect Ratio Test
            aspect_ratio_ok[i] = 0
        else:
            aspect_ratio_ok[i] = 1
    try:
        cmax = blobs[0]
    except:
        cmax = -1
    for c in range(0,len(blobs)):
        if (aspect_ratio_ok[c] == 1): #Only look through good aspect ratios
            if (int(blobs[c].w()) > int(cwmax)): #Target largest object with ok aspect ratio
                cwmax=blobs[c].w()
                cmax=blobs[c]
        print(cmax)
    try:
        if(abs(cmax.w()-cmax.h()) > (cmax.w()/4)): #Aspect Ratio Test
            cmax = -2
    except:
        pass
    try:
        img.draw_circle(cmax.cx(), cmax.cy(), int(cmax.w()/2), color = (255, 0, 0)) #Draw circle
        if (cmax.cx() >= (img.width()/2)): #colored led depends on side of image, to debug
            torled = True
            togled = False
        else:
            torled = False
            togled = True
        allbits = cmax.cx() #Update bits
    except:
        torled = False
        togled = False
        allbits = 511 #Update bits with special value 11111111
    #Update LEDs
    if(torled):
        redled.on()
    else:
        redled.off()
    if(togled):
        grnled.on()
    else:
        grnled.off()
    try:
        i2c.send(allbits, timeout=5) #Send over i2c
    except:
        pass
    print(clock.fps())
