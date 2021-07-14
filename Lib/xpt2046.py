from time import sleep_ms
from machine import SPI, Pin
from micropython import const

T_GETX  = const(0xd0)  ## 12 bit resolution
T_GETY  = const(0x90)  ## 12 bit resolution
T_GETZ1 = const(0xb8)  ## 8 bit resolution
T_GETZ2 = const(0xc8)  ## 8 bit resolution
#
X_LOW  = const(10)     ## lowest reasonable X value from the touchpad
Y_HIGH = const(4090)   ## highest reasonable Y value

class XPT2046:
    DEFAULT_CAL = (-3917, -0.127, -3923, -0.1267, -3799, -0.07572, -3738,  -0.07814)

    def __init__(self, spi=None, *, confidence=5, margin=50, delay=10, calibration=None):
        if spi is None:
            raise IOError("The SPI object has to be supplied")
        else:
            self.spi = spi
        self.recv = bytearray(3)
        self.xmit = bytearray(3)
        self.ready = False
        self.touched = False
        self.x = 0
        self.y = 0
        self.buf_length = 0
        cal = XPT2046.DEFAULT_CAL if calibration is None else calibration
        self.touch_parameter(confidence, margin, delay, cal)

    def touch_parameter(self, confidence=5, margin=50, delay=10, calibration=None):
        confidence = max(min(confidence, 25), 5)
        if confidence != self.buf_length:
            self.buff = [[0,0] for x in range(confidence)]
            self.buf_length = confidence
        self.delay = max(min(delay, 100), 5)
        margin = max(min(margin, 100), 1)
        self.margin = margin * margin # store the square value
        if calibration:
            self.calibration = calibration

    def raw_touch(self):
        x  = self.touch_talk(T_GETX, 12)
        y  = self.touch_talk(T_GETY, 12)
        if x > X_LOW and y < Y_HIGH:  # touch pressed?
            return (x, y)
        else:
            return None

    def touch_talk(self, cmd, bits):
        self.xmit[0] = cmd
        self.spi.write_readinto(self.xmit, self.recv)
        return (self.recv[1] * 256 + self.recv[2]) >> (15 - bits)

