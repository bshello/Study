T = int(input())

for t in range(1, T+1):
    x, y = map(int, input().split())
    print(f'Case #{t}: {x} + {y} = {x+y}')