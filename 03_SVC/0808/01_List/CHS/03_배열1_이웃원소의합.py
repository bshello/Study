T = int(input())
for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    max_num = 0
    for j in range(0, N - 1):
        result = nums[j] + nums[j + 1]
        if max_num == 0:
            max_num = result
        else:
            if max_num < result:
                max_num = result
    print(f'#{i + 1} {max_num}')