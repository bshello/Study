h, m = map(int, input().split())
if m-45<0:
    if h == 0:
        h = 23
    else:
        h = h-1
    m = m+15
else:
    m = m-45
print(h, m)