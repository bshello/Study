c , d = map(int, input().split())
c = bool(c)
d = bool(d)
print((c and not d) or (not c and d))