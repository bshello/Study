
nums = list(map(int, input().split()))
total = 1
number = 0
for i in range(0, len(nums)):
    if nums[i] == nums[i-1]:
        total += 1
        number = nums[i]

if total == 4:
    print(10000+number*1000)
elif total == 2:
    print(1000+number*100)
else:
    print(max(nums)*100)




# if x == y == z:
#     print(10000+x*1000)
# elif x != y != z:
#     print(max(x, y, z)*100)
# else:
