h, b, c, s = map(int, input().split())
m = h*b*c*s/8/1024/1024
mem = round(m,1)
print(f'{mem} MB' )
