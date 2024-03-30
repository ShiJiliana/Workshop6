square = input()
let = square[0]
num = int(square[1])

white = ['a', 'c', 'e', 'g']
black = ['b', 'd', 'f', 'h']

if num % 2 == 0:
    if let in white:
        print('белый')
    elif let in black:
        print('чёрный')
    else:
        print('ошибка')
else:
    if let in white:
        print('чёрный')
    elif let in black:
        print('белый')
    else:
        print('ошибка')