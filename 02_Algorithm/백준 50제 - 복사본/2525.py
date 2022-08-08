x, y = map(int, input().split())
m = int(input())

x += m // 60
y += m % 60
if y >= 60:
  x += 1
  y = y - 60
if x >= 24:
  x = x-24
  
print(x , y)