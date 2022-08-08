x, y, z = map(int, input().split())
c = int(input())

total = x*3600 + y*60 + z + c

x = (total // 3600) % 24
y = (total % 3600) // 60
z = (total % 3600) % 60

print(x, y, z)