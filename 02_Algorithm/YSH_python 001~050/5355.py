for T in range(int(input())):
    lst = []
    x, *lst = input().split()
    if '.' in x:
        x = float(x)
    else:
        x = int(x)

    for i in lst:
        if i == '@':
            x *= 3
        elif i == '%':
            x += 5
        else:
            x -= 7
    print(format(x, '.2f'))