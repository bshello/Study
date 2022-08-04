pan = []
for idx in range(10):
    d = list(map(int, input().split()))
    pan.append(d)
pan[1][1] = 9
count = 1
stop = 0
for i in range(1,len(pan)):
    if stop == 1:
        break
    else:
        for j in range(count,len(pan[i])):    
            if pan[i][j] == 1:
                count = j-1
                break
            elif pan[i][j] == 2:
                pan[i][j] = 9
                stop += 1
                break
            else:
                pan[i][j] = 9

for row in range(len(pan)):
    for col in range(len(pan[row])):
        print(pan[row][col], end=" ")
    print("")
