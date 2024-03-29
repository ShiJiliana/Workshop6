a, b = map(int, input().split('x'))
c, d, e = map(int, input().split('x'))
hole = a * b
lng_edg = max(c, d, e)
if lng_edg == c:
    stone = d * e
elif lng_edg == d:
    stone = c * e
else:
    stone = d * c

if stone < hole:
    print('да')
else:
    print('нет')