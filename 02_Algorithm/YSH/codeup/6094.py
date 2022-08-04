n = int(input())

lst = list(map(int, input().split()))

min = lst[0]
for i in lst[1:]:
    if i < min:
        min = i
print(min)