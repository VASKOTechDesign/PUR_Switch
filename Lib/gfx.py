class GFX:

    def __init__(self, width, height, pixel, hline=None, vline=None):
        self.width = width
        self.height = height
        self._pixel = pixel
        if hline is None:
            self.hline = self._slow_hline
        else:
            self.hline = hline
        if vline is None:
            self.vline = self._slow_vline
        else:
            self.vline = vline

    def _slow_hline(self, x0, y0, width, *args, **kwargs):
        if y0 < 0 or y0 > self.height or x0 < -width or x0 > self.width:
            return
        for i in range(width):
            self._pixel(x0+i, y0, *args, **kwargs)

    def _slow_vline(self, x0, y0, height, *args, **kwargs):
        if y0 < -height or y0 > self.height or x0 < 0 or x0 > self.width:
            return
        for i in range(height):
            self._pixel(x0, y0+i, *args, **kwargs)

    def rect(self, x0, y0, width, height, *args, **kwargs):
        if y0 < -height or y0 > self.height or x0 < -width or x0 > self.width:
            return
        self.hline(x0, y0, width, *args, **kwargs)
        self.hline(x0, y0+height-1, width, *args, **kwargs)
        self.vline(x0, y0, height, *args, **kwargs)
        self.vline(x0+width-1, y0, height, *args, **kwargs)

    def line(self, x0, y0, x1, y1, *args, **kwargs):
        steep = abs(y1 - y0) > abs(x1 - x0)
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        dx = x1 - x0
        dy = abs(y1 - y0)
        err = dx // 2
        ystep = 0
        if y0 < y1:
            ystep = 1
        else:
            ystep = -1
        while x0 <= x1:
            if steep:
                self._pixel(y0, x0, *args, **kwargs)
            else:
                self._pixel(x0, y0, *args, **kwargs)
            err -= dy
            if err < 0:
                y0 += ystep
                err += dx
            x0 += 1
