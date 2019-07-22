from PIL import Image


class Rasterizer:
    def __init__(self, extent, clear_color):
        self.extent = extent
        self._img = Image.new('RGB', extent, clear_color)
        self._pixels = self._img.load()

    def draw_line(self, a, b, color):
        steep = False
        if abs(a.x - b.x) < abs(a.y - b.y):
            a.x, a.y = a.y, a.x
            b.x, b.y = b.y, b.x
            steep = True
        if a.x > b.x:
            a.swap_with(b)

        x_len = abs(b.x - a.x)
        y_len = abs(b.y - a.y)

        y = a.y
        y_step = 1 if b.y - a.y > 0 else -1
        error = 0

        for x in range(a.x, b.x):
            if steep:
                self._pixels[y, x] = color
            else:
                self._pixels[x, y] = color

            error += y_len
            if error * 2 >= x_len:
                y += y_step
                error -= x_len

    def draw_triangle(self, vertices, color):
        vertices.sort(key=lambda v: v.y)

        min = vertices[0]
        mid = vertices[1]
        max = vertices[2]

        total_height = max.y - min.y

        # a - longer edge of triangle: from min to max
        # b - consists of two edges: from min to mid, from mid to max

        # draws first segment
        segment_height = mid.y - min.y
        for y in range(min.y, mid.y):
            y_offset = y - min.y

            ax = min.x + (max.x - min.x) * y_offset // total_height
            bx = min.x + (mid.x - min.x) * y_offset // segment_height

            x_range = range(ax, bx) if ax < bx else range(bx, ax)
            for x in x_range:
                self._pixels[x, y] = color

        # draws second segment
        segment_height = max.y - mid.y
        for y in range(mid.y, max.y):
            ay_offset = y - min.y
            by_offset = y - mid.y

            ax = min.x + (max.x - min.x) * ay_offset // total_height
            bx = mid.x + (max.x - mid.x) * by_offset // segment_height

            x_range = range(ax, bx) if ax < bx else range(bx, ax)
            for x in x_range:
                self._pixels[x, y] = color

    def show_image(self):
        self._img.show()
