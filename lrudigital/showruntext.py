#!/usr/bin/env python
import time
import sys

import options

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

if len(sys.argv) < 2:
    sys.exit("Require an text argument")
else:
    text = sys.argv[1]

matrix = RGBMatrix(options = options.options)

offscreen_canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("fonts/7x13.bdf")
textColor = graphics.Color(255, 255, 0)
pos = offscreen_canvas.width

onetime = True

try:
    print("Press CTRL-C to stop.")
    while True:
        offscreen_canvas.Clear()
        len = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor, text)
        pos -= 1
        if (pos + len < 0):
            pos = offscreen_canvas.width
            if (onetime):
                sys.exit(0) # This will end after one go

        time.sleep(0.03)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
except KeyboardInterrupt:
    sys.exit(0)