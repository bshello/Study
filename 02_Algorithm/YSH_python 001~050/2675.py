T = int(input())

for i in range(T):
  str = ''
  x, y = input().split()
  for i in y:
    str += i * int(x)
  
  print(str)