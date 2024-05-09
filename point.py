from rectangle import Rectangle


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle: Rectangle):
        if (
            rectangle.point1.x < self.x < rectangle.point2.x
            and rectangle.point1.y < self.y < rectangle.point2.y
        ):
            return True
        else:
            return False
