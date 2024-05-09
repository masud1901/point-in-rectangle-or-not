from rectangle import Rectangle
from turtle import Turtle
import turtle


class GuiRectangle(Rectangle):  # Is a relationship  i.e. GuiRectangle  is  a rectangle

    def draw(
        self,
        canvas: Turtle,
    ) -> None:

        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        width = abs(self.point1.x - self.point2.x)
        length = abs(self.point1.y - self.point2.y)

        canvas.pendown()
        canvas.forward(length)
        canvas.left(90)

        canvas.forward(width)
        canvas.left(90)

        canvas.forward(length)
        canvas.left(90)

        canvas.forward(width)
