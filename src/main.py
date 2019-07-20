from rasterizer import Rasterizer
from utils.point import Point


def do():
    rasterizer = Rasterizer((1920, 1080), 'black')
    rasterizer.draw_line(Point(1600, 1000), Point(100, 100), (0, 200, 0))
    rasterizer.show_image()


if __name__ == "__main__":
    do()
