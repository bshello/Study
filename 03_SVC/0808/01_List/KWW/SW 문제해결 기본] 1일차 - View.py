for tc in range(1,11):
    leng = input()
    apt=[]
    ans = 0
    a = list(map(int, input().split()))
 
    for i in a:
        apt.append(i)
 
    for vw in range(2,len(apt)-2):
        if apt[vw] > apt[vw-2] and apt[vw] > apt[vw-1] and apt[vw] > apt[vw+2]  and apt[vw] > apt[vw+1]:
 
            if apt[vw]-apt[vw-2]>apt[vw]-apt[vw-1]:
                l = apt[vw]-apt[vw-1]
            else:
                l = apt[vw]-apt[vw-2]
 
            if apt[vw]-apt[vw+2]>apt[vw]-apt[vw+1]:
                r = apt[vw]-apt[vw+1]
            else:
                r = apt[vw]-apt[vw+2]
                 
            if l>r:
                temp = r
            else:
                temp = l
            ans+=temp
 
    print(f'#{tc} {ans}')
