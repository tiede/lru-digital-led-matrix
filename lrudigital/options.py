from rgbmatrix import RGBMatrix, RGBMatrixOptions

ROWS = 32
COLS = 64

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = ROWS
options.cols = COLS
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.disable_hardware_pulsing=True
options.gpio_slowdown=3