import turtle
import math

x1, y1, r1 = map(int, input('Введите координаты центра и радиус №1 ').split())
x2, y2, r2 = map(int, input('Введите координаты центра и радиус №2 ').split())

long = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if long > r1 + r2:
    print('Окружности лежат одна вне другой, не касаясь')

elif long == r1 + r2:
    print('Окружности имеют внешнее касание')

elif long < r1 + r2 and long > abs(r1 - r2):
    print('Окружности пересекаются')

elif long == abs(r1 - r2):
    print('Окружности имеют внутреннее касание')

elif long < abs(r1 - r2):
    print('Одна окружность лежит внутри другой, не касаясь')

turtle.up()
turtle.setposition(x1, y1 - r1)
turtle.down()
turtle.circle(r1)

turtle.up()
turtle.setposition(x2, y2 - r2)
turtle.down()
turtle.circle(r2)

turtle.hideturtle()
turtle.down()