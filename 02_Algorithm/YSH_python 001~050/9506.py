while True:
    n = int(input())
    if n == -1:
        break
    if n == sum([x for x in range(1, n) if n % x ==0]):
        print(f'{n} = ', end="")
        nums = [str(x) for x in range(1, n) if n % x == 0]
        print(*nums, sep=" + ")
            
            
    else:
        print(f'{n} is NOT perfect.')