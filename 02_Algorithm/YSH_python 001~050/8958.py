n = int(input())

for N in range(n):
    total = 0
    count = 0
    ox = input()
    for i in ox:
        if i == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)