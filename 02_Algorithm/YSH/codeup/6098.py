
lst = []

for i in range(10):
    nums = list(map(int, input().split()))
    lst.append(nums)
lst[1][1] = 9
x, y = 1, 1
n = 0
while n != 1:
    try:
        if lst[x][y+1] == 0:
            lst[x][y+1] = 9
            y += 1
        elif lst[x][y+1] == 2:
            lst[x][y+1] = 9
            n = 1
        else:
            try:
                if lst[x+1][y] == 0:
                    lst[x+1][y] = 9
                    x += 1
                elif lst[x+1][y] == 1:
                    break
                else:
                    lst[x+1][y] = 9
                    n = 1
            except:
                print("out of range")    # 8,8 을 break으로 둬야 했던 것 같은데.. 실패하는 케이스도 없는 것 같다

    except:
        print("out of range")
    
for i in lst:
    print(*i)