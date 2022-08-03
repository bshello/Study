n = int(input())
temp = 0
for i in range(1,n):
    if temp>=n:
        print(i-1)
        break
    else:
        temp+=i    
