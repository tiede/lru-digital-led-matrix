#!/usr/bin/env python
import time
import sys
import csv

import options

from rgbmatrix import RGBMatrix, RGBMatrixOptions

if len(sys.argv) < 2:
    sys.exit("Require an csv argument")
else:
    csv_filename = sys.argv[1]

matrix = RGBMatrix(options = options.options)

with open(csv_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        color_offset = 0
        for cols_count in range(0, options.COLS - 1):
            red = int(row[cols_count + color_offset])
            color_offset += 1
            green = int(row[cols_count + color_offset])
            color_offset += 1
            blue = int(row[cols_count + color_offset])
            #print ("R {0} G {1} B {2}".format(red, green, blue))
            matrix.SetPixel(cols_count, line_count, red, green, blue)
        line_count += 1

try:
    print("Press CTRL-C to stop.")
    time.sleep(30)
except KeyboardInterrupt:
    sys.exit(0)