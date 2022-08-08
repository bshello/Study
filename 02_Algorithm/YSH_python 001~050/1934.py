n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    max = 0 #최대공약수
    for j in range(min(x,y), 0, -1):
        if x % j == 0 and y % j == 0:
            max = j
            break
    print(int((x*y)/max))  # 두수의 곱을 최대공약수로 나눠준다
    
