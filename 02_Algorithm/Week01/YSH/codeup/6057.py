a, b = map(int, input().split())
a, b = bool(a), bool(b)

print((a and b) or (not a and not b))