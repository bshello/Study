d = []
pos = []
x = []
y = []
for i in range(1,20):
    n = list(map(int, input().split()))
    d.append(n)
n = int(input())
for j in range(n):
    a = list(map(int,input().split()))
    pos.append(a)
for k in range(len(pos)):
    x.append(pos[k][0])
    y.append(pos[k][1])

for p in range(len(x)):
    for l in range(len(d)):
        if d[l][y[p]-1] == 1:
            d[l][y[p]-1] = 0
        else:
            d[l][y[p]-1] = 1
        if d[x[p]-1][l] == 1:
            d[x[p]-1][l] = 0
        else:
            d[x[p]-1][l] = 1

for a in range(len(d)):
    for b in range(len(d[a])):
        print(d[a][b], end=" ")
    print("") 
