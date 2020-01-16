# Color Binary Filter Example
#
# This script shows off the binary image filter. You may pass binary any
# number of thresholds to segment the image by.(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)(19, 88, -31, 45, 9, 127)

import sensor, image, time, pyb

sensor.reset()
sensor.set_framesize(sensor.QQVGA)
sensor.set_pixformat(sensor.RGB565)
sensor.skip_frames(time = 2000)
clock = time.clock()

redled = pyb.LED(1)
grnled = pyb.LED(2)

torled = 0
togled = 0

# Use the Tools -> Machine Vision -> Threshold Edtor to pick better thresholds.
red_threshold = (0, 100, -30, 22, 28, 127) # L A B

while(True):

    # Test red threshold
    clock.tick()
    img = sensor.snapshot()
    img.binary([red_threshold])

    img.erode(8,8)

    cwmax = 0
    blobs = img.find_blobs([(100,255),(100,255),(100,255)])
    try:
        cmax = blobs[0]
    except:
        cmax = -1
    for c in blobs:
        if (int(c.w()) > int(cwmax)):
            cwmax=c.w()
            cmax=c
        print(cmax)
    try:
        if(abs(cmax.w()-cmax.h()) > (cmax.w()/8)):
            cmax = -2
    except:
        pass
    try:
        img.draw_circle(cmax.cx(), cmax.cy(), int(cmax.w()/2), color = (255, 0, 0))
        if (cmax.cx() >= (img.width()/2)):
            torled = True
            togled = False
        else:
            torled = False
            togled = True
    except:
        torled = False
        togled = False
    if(torled):
        redled.on()
    else:
        redled.off()
    if(togled):
        grnled.on()
    else:
        grnled.off()
    print(clock.fps())
