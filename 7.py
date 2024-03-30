k = int(input())

ans = 'нет'

if k % 5 == 0 or k % 7 == 0:
    ans = 'да'

if k >= 5:
    for i in range(k//5):
        for j in range(k//7):
            if k == 5*i + 7*j:
                ans = 'да'

print(ans)