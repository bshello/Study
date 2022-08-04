
lst = []

for i in range(10):
    nums = list(map(int, input().split()))
    lst.append(nums)
lst[1][1] = 9
x, y = 1, 1
n = 0
while n != 1:
    if lst[x][y+1] == 0:
        lst[x][y+1] = 9
        y += 1
    elif lst[x][y+1] == 2:
        lst[x][y+1] = 9
        n = 1

    else:
        if lst[x+1][y] == 0:
            lst[x+1][y] = 9
            x += 1
        elif lst[x+1][y] == 2:
            lst[x+1][y] = 9
            n = 1
        elif x == 8 and y == 8:
            n = 1
    
for i in lst:
    print(*i)