clock = [300, 60, 10]
n = int(input())

if n % 10 == 0:
    for i in clock:
        print(n // i, end=' ')
        n %= i
else:
    print(-1)
