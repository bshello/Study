import sys

n = int(sys.stdin.readline())

s = 2
while n != 1:
    if n % s == 0:
        n = n / s
        print(s)
    else:
        s += 1


# if n != 1:
#     s = 2 # 소수 설정
#     while n != 1:
#         for i in range(2, s+1):
#             if s % i == 0 and s != i:  # 소수인지 확인
#                 s += 1
#                 break
#             elif s == i:
#                 if n % s == 0:    #소수가 맞으면 나누기 시작
#                  n = n / s
#                  print(s)
#                 else:
#                     s += 1