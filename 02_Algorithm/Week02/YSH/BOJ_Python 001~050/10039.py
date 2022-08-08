total = 0

for i in range(5):
    n = int(input())
    if n > 40:
        total += n
    else:
        total += 40
print(round(total / 5))