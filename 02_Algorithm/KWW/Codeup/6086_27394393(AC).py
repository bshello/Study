n = int(input())
temp = 0
if n == 1:
    print (n)
else:
    for i in range(n):
        if temp>=n:
            print(temp)
            break
        else:
            temp+=i 
