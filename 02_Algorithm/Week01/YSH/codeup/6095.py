
d= []
for i in range(19):
    d.append([])
    for j in range(19):
        d[i].append(0)

T = int(input())

for t in range(1, T+1):
    x, y = map(int, input().split())
    d[x-1][y-1] = 1

for k in d:
    print(*k) 