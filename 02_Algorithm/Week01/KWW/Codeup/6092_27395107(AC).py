n = input()
a = list(map(int, input().split()))
alist = {}
for i in a:
    if i in alist:
        alist[i] +=1
    else:
        alist.update({i:1})
for i in range(1, 24):
    if i in alist.keys():
        print(alist[i], end=" ")
    else:
        print(0, end = " ")

