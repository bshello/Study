T = int(input())

for t in range(T):
    x, y, z = map(int, input().split())

    if x < y - z:
        print('advertise')
    elif x == y - z:
        print('does not matter')
    else:
        print('do not advertise')