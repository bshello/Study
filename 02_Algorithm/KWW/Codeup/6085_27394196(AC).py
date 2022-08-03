w, h, b = map(int, input().split())
m = w*h*b/8/1024/1024
mem = format(m,".2f")
print(f'{mem} MB' )
