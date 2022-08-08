a = 0
b = 0
c = 0
d = 0

n = int(input())
for t in range(n):
    x, y = map(int, input().split())
    a += (x > 0 and y > 0)
    b += (x < 0 and y > 0)
    c += (x < 0 and y < 0)
    d += (x > 0 and y < 0)
print(f'Q1: {a}')
print(f'Q2: {b}')
print(f'Q3: {c}')
print(f'Q4: {d}')
print(f'AXIS: {n-(a+b+c+d)}')
