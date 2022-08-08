T = int(input())
for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    max_index = 0
    min_index = 0
    for j in range(0, N):
        if max_index == 0 and min_index == 0:
            max_index = j + 1
            min_index = j
        else:
            if nums[max_index] <= nums[j]:
                max_index = j
            if nums[min_index] > nums[j]:
                min_index = j
    max_index += 1
    min_index += 1
    answer = max_index - min_index
    if answer < 0:
        answer = - answer
    print(f'#{i + 1} {answer}')