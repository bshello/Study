a, b, c = map(int, input().split())
for i in range(1,1000000):
    if i%a == 0:
        if i%b == 0:
            if i%c == 0:
                day = i
                break
print(day)   
