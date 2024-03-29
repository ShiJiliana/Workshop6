import turtle
x1, y1, x2, y2 = map(int, input('Введите координаты вверхней левой и '
                                'правой нижней вершины прямоугольника №1 ').split())
x3, y3, x4, y4 = map(int, input('Введите координаты вверхней левой и '
                                'правой нижней вершины прямоугольника №2 ').split())
rect1 = [x1, y1, x2, y2]
rect2 = [x3, y3, x4, y4]

long1 = x2 - x1
height1 = y1 - y2
long2 = x4 - x3
height2 = y3 - y4

if (rect1[0] > rect2[0] and rect1[1] < rect2[1] and rect1[2] < rect2[2] and rect1[3] > rect2[3]
        or rect2[0] > rect1[0] and rect2[1] < rect1[1] and rect2[2] < rect1[2] and rect2[3] > rect1[3]):
    print('Один прямоугольник лежит внутри другого, не касаясь')

elif rect1[2] < rect2[0] or rect2[2] < rect1[0] or rect1[3] < rect2[1] or rect2[3] < rect1[1]:
    print('Прямоугольники лежат вне друг друга, не касаясь')

elif rect1[2] == rect2[0] or rect2[2] == rect1[0] or rect1[3] == rect2[1] or rect2[3] == rect1[1]:
    print('Прямоугольники имеют касание')

elif ((rect1[0] <= rect2[0] <= rect1[2] or rect2[0] <= rect1[0] <= rect2[2]) and
        (rect1[1] <= rect2[1] <= rect1[3] or rect2[1] <= rect1[1] <= rect2[3])):
    print('Прямоугольники имеют пересечение')

else:
    print('Другое относительное расположение')

turtle.up()
turtle.setposition(x1, y1)
turtle.down()
turtle.forward(long1)
turtle.right(90)
turtle.forward(height1)
turtle.right(90)
turtle.forward(long1)
turtle.right(90)
turtle.forward(height1)
turtle.right(90)

turtle.up()
turtle.setposition(x3, y3)
turtle.down()
turtle.forward(long2)
turtle.right(90)
turtle.forward(height2)
turtle.right(90)
turtle.forward(long2)
turtle.right(90)
turtle.forward(height2)
turtle.right(90)

turtle.hideturtle()
turtle.done()