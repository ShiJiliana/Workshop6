import math
a, b = map(int, input().split('x'))
d = math.sqrt(a**2 + b**2)
if not d <= 13:
    print('нет')
else:
    print('да')
