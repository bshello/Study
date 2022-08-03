a = list(map(int, input().split()))
num = a[0]
for i in range(1,len(a)):   
    if a[i]< num:
        num = a[i]
print(num)
