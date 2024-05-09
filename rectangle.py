from point import Point


class Rectangle:

    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return abs(self.point1.x - self.point2.x) * abs(self.point1.y - self.point2.y)


