from __future__ import absolute_import

from src.rasterizer import Rasterizer
from src.utils.point import Point


def do():
    rasterizer = Rasterizer((1920, 1080), (0, 0, 0))

    vertices = [Point(50, 1000), Point(1700, 100), Point(1800, 800)]
    rasterizer.draw_triangle(vertices, (190, 10, 70))

    rasterizer.draw_line(Point(0, 0), Point(1919, 1079), (200, 250, 20))

    vertices = [Point(150, 60), Point(1200, 190), Point(400, 700)]
    rasterizer.draw_triangle(vertices, (50, 250, 170))

    rasterizer.show_image()


if __name__ == "__main__":
    do()
