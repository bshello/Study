for i in range(10):
    N = int(input())
    nums = list(map(int, input().split()))
    view = 0
    for j in range(2, N - 2):
        A = nums[j] - nums[j - 2]
        B = nums[j] - nums[j - 1]
        C = nums[j] - nums[j + 1]
        D = nums[j] - nums[j + 2]
        new_list = [A, B, C, D]
        min_view = new_list[0]
        for k in new_list:
            if k < min_view:
                min_view = k
        if A > 0 and B > 0 and C > 0 and D > 0:
            view += min_view
    print(f'#{i + 1} {view}')