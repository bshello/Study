
x1 = []
y1 = []
for i in range(3):
    x, y = map(str, input().split())
    x1.append(x)
    y1.append(y)
a = ''
b = ''

for j in range(3):
    if x1.count(x1[j]) == 1:
        a = x1[j]
    if y1.count(y1[j]) == 1:
        b = y1[j]
print(a, b)
        

