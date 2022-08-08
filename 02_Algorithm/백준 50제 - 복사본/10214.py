for t in range(int(input())):
    ys = 0
    kr = 0
    for T in range(9):
        x, y = map(int, input().split())
        ys += x
        kr += y
    if ys > kr:
        print('Yonsei')
    elif kr > ys:
        print('Korea')
    else:
        print("Draw")
