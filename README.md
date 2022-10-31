# lru-digital-led-matrix

## The code uses the rpi-rgb-led-matrix library

### Install Python dev tools

```
sudo apt-get update  && sudo apt-get install -y git python3-dev python3-pillow
```

### Install rpi-rgb-led-matrix

```
git clone https://github.com/hzeller/rpi-rgb-led-matrix.git
cd rpi-rgb-led-matrix/
make build-python  PYTHON=$(which python3)
sudo make install-python PYTHON=$(which python3)
```

## Options for the rpi-rgb-led-matrix

On never RPI you need to change the speed: gpio_slowdown=3
Set the hat to the correct version: hardware_mapping = 'adafruit-hat'
Disable hardware pulses if you have not disabled the sound: disable_hardware_pulsing=True