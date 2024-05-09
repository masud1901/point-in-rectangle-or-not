from turtle import Turtle
from point import Point


class GuiPoint(Point):

    def draw(self, canvas: Turtle):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(10, "blue")
