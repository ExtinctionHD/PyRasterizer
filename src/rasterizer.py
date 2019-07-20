from PIL import Image


class Rasterizer:
    def __init__(self, extent, clear_color):
        self.extent = extent
        self._img = Image.new('RGB', extent, clear_color)
        self._pixels = self._img.load()

    def draw_line(self, a, b, rgb):
        steep = False
        if abs(a.x - b.x) < abs(a.y - b.y):
            a.x, a.y = a.y, a.x
            b.x, b.y = b.y, b.x
            steep = True
        if a.x > b.x:
            a.swap_with(b)

        delta_x = abs(b.x - a.x)
        delta_y = abs(b.y - a.y)

        error = 0
        delta_error = delta_y
        y = a.y
        y_direction = 1 if b.y - a.y > 0 else -1

        for x in range(a.x, b.x):
            if steep:
                self._pixels[y, x] = rgb
            else:
                self._pixels[x, y] = rgb

            error += delta_error
            if error * 2 >= delta_x:
                y += y_direction
                error -= delta_x

    def show_image(self):
        self._img.show()
