a = list(map(int, input().split()))
if bool(a[0]) == False:
    if bool(a[1]) == False:
        print(True)
    else:
        print(False)
else:
    print(False)
