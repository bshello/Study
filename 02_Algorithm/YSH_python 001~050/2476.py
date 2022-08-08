m = []
for i in range(int(input())):
    nums = list(map(int, input().split()))
    if len(set(nums)) == 1:
        m.append(nums[0]*1000+10000)
    elif len(set(nums)) == 2:
        m.append(sorted(nums)[1]*100+1000)
    else:
        m.append(max(nums)*100)
print(max(m))