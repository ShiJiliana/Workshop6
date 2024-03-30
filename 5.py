step = input()
let1 = step[0]
let2 = step[3]

num1 = step[1]
num2 = step[4]

name_line = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
num_line = ['1', '2', '3', '4', '5', '6', '7', '8']

print(let1, let2, num1, num2)

if let1 == let2 or num1 == num2:
    print('ошибка')

elif (abs(name_line.index(let1) - name_line.index(let2)) == 1
      and abs(num_line.index(num1) - num_line.index(num2)) == 2):
    print('ход возможен')

elif (abs(name_line.index(let1) - name_line.index(let2)) == 2
      and abs(num_line.index(num1) - num_line.index(num2)) == 1):
    print('ход возможен')

else:
    print('ошибка')

