a = list(map(int, input().split()))

c = bool(a[0])
d = bool(a[1])
print((c and (not d)) or ((not c) and d))
