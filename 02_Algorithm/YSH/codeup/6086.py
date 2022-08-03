n = int(input())
total = 0
c = 1

while True:
    if total >= n:
        print(total)
        break
    else:
        total += c
        c += 1