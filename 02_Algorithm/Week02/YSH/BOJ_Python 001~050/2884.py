x, y = map(int, input().split())

c = x*3600 + y*60 - 45*60
x = c // 3600 % 24
y = c % 3600 // 60

print(x, y)