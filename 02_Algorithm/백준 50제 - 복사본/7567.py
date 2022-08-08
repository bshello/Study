n = input()
total = 10
for i in range(1, len(n)):
    if n[i-1] == n[i]:
        total += 5
    else:
        total+= 10

print(total)