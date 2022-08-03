n = int(input())
lst = list(map(int, input().split()))

nums = [0]*23

for i in lst:
    nums[i-1] = nums[i-1] + 1

print(*nums)