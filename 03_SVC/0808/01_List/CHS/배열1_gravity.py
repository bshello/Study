T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    max_score = 0
    for i in range(0, N - 1):
        cnt = 0
        for j in range(i + 1, N):
            if nums[i] <= nums[j]:
                cnt += 1
        score = N - 1 - i - cnt
        if score > max_score:
            max_score = score
    print(f'#{_ + 1} {max_score}')