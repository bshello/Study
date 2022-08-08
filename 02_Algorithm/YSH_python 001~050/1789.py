n = int(input())
total = 0
count = 0
while True:
    count += 1
    total += count
    if total - n > 0:     #total이 n을 넘었을 때 total - n 의 값은 무조건 total 전에 포함이 되기 때문에 카운트에서 하나 차감.
        print(count-1)
        break
