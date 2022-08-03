r, g, b = map(int, input().split())
color = list()

for i in range(r):
    for j in range(g):
        for k in range(b):
            colist = [i, j, k]
            color.append(colist)

for l in color:
    for m in range(len(l)):
        if m == 2:
            print(l[m])
        else:
            print(l[m], end = " ")
print(r*g*b)
