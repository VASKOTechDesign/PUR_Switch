
try:
    import ustruct
except ImportError:
    import struct as ustruct

import time


class BitmapFont:

    def __init__(self, width, height, pixel, font_name):
        self._width = width
        self._height = height
        self._pixel = pixel
        self._font_name = font_name

    def init(self):
        self._font = open('/Fonts/'+self._font_name, 'rb')
        self._font_width, self._font_height = ustruct.unpack('BB', self._font.read(2))

    def deinit(self):
        self._font.close()

    def __enter__(self):
        self.init()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.deinit()

    def draw_char(self, ch, x, y, _landscape, *args, **kwargs):
        if _landscape == 0:
            if x < -self._font_width or x >= self._width or y < -self._font_height or y >= self._height:
                return
        if _landscape == 1:
            if x < -self._font_width or x >= self._height or y < -self._font_height or y >= self._width:
                return
        for char_x in range(self._font_width):
            self._font.seek(2 + (ord(ch) * self._font_width) + char_x)
            line = ustruct.unpack('B', self._font.read(1))[0]
            for char_y in range(self._font_height):
                if _landscape == 0: 
                  if (line >> char_y) & 0x1:
                      self._pixel(x + char_x, y + char_y, *args, **kwargs)
                if _landscape == 1: 
                  if (line >> char_y) & 0x1:
                      self._pixel((y + self._font_height) - char_y - 1, x + (char_x), *args, **kwargs)
                      
    def text(self, text, x, y, _landscape, *args, **kwargs):
        for i in range(len(text)):
            self.draw_char(text[i], x + (i * (self._font_width + 1)), y, _landscape,
                           *args, **kwargs)
                           
    def width(self, text):
        return len(text) * (self._font_width + 1)