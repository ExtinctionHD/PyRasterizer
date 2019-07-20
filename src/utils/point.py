class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        result = Point(self.x, self.y)
        result.x += other.x
        result.y += other.y
        return result

    def __sub__(self, other):
        result = Point(self.x, self.y)
        result.x -= other.x
        result.y -= other.y
        return result

    def swap_with(self, other):
        self.x, other.x = other.x, self.x
        self.y, other.y = other.y, self.y



