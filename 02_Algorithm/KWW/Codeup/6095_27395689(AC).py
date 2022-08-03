n = int(input())
inp = []
for i in range(n):
    a = list(map(int, input().split()))
    inp.append(a)
d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
for i in range(len(inp)):
    d[inp[i][0]][inp[i][1]] = 1
for x in range(1,len(d)):
    for y in range(1,len(d[x])):
        print(d[x][y], end=" ")
    print("")
