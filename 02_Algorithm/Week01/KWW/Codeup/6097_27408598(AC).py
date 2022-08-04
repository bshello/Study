h, w = map(int, input().split())
n = int(input())
temp = []
l = []
d = []
x = []
y = []
pan = []

for a in range(n):
    temp.append(list(map(int, input().split())))

for b in range(len(temp)):
    l.append(temp[b][0])
    d.append(temp[b][1])
    x.append(temp[b][2])
    y.append(temp[b][3])

for i in range(h):
    pan.append([])
    for j in range(w):
        pan[i].append(0)

for idx in range(len(l)):
    for k in range(l[idx]):
        if d[idx] == 0:
            pan[x[idx]-1][y[idx]+k-1] = 1
        if d[idx] == 1:
            pan[x[idx]+k-1][y[idx]-1] = 1

for row in range(len(pan)):
    for col in range(len(pan[row])):
        print(pan[row][col], end=" ")
    print("")
