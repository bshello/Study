x, y, z = map(int, input().split())

d = 1
while d % x !=0 or d % y !=0 or d % z !=0:
    d += 1

print(d) 
