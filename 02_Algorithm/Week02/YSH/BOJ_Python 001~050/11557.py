n = int(input())

for i in range(n):
    N = int(input())
    answer = ""
    max = 0
    for j in range(N):
        x, y = input().split()
        if int(y) > max:
            max = int(y)
            answer = x
    print(answer)
