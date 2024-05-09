from point import Point
from random import randint
from guiRectangle import GuiRectangle
from guiPoint import GuiPoint
import turtle


rectangle = GuiRectangle(
    Point(randint(0, 200), randint(0, 200)), Point(randint(0, 200), randint(0, 200))
)


print(
    f"Rectangle Coordinates: {rectangle.point1.x} {rectangle.point1.y} \
    and {rectangle.point2.x} {rectangle.point2.y}"
)


user_points = GuiPoint(int(input("Guess x: ")), int(input("Guess y: ")))
user_area = float(input("Guess the rectangle area: "))

print(
    f"Your point was inside the rectangle: \
    {user_points.falls_in_rectangle(rectangle=rectangle)} "
)
print(f"Your area was off by: {rectangle.area()- user_area}")

myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)

user_points.draw(canvas=myturtle)
turtle.done()
