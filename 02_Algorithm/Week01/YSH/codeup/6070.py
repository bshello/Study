n = int(input())

if n // 3 == 1:
    print('spring')
elif 5 < n < 9:
    print('summer')
elif n // 3 == 3:
    print('fall')
else:
    print('winter')