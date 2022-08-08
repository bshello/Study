n = input()
line = input()
a = 0
for i in line:
    if i == 'A':
        a += 1
if a > len(line) - a:
    print('A')
elif a == len(line) - a:
    print('Tie')
else:
    print('B')

