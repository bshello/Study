n = input()
a = list(map(int, input().split()))
temp = 10000
for i in a:
    if i<temp:
        temp = i
print(temp)


