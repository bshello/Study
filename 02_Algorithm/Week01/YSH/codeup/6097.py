x, y = map(int, input().split())
T = int(input())

lst = []
for i in range(x):
    lst.append([])
    for j in range(y):
        lst[i].append(0)


for t in range(T):
    a, b, c, d = map(int, input().split())
    
    if b == 0:
        for k in range(a):
            lst[c-1][d-1+k] = 1
    else:
        for k in range(a):
            lst[c-1+k][d-1] = 1

for p in lst:
    print(*p)