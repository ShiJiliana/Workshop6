n, k, m = map(int, input().split())
if n > k:
    if n % k == 0:
        visits = 2 * (n // k)
    else:
        visits = 2 * ((n // k) + 1)
else:
    visits = 2

print(m * visits)