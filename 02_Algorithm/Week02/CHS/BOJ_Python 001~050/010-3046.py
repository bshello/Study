import sys

input = sys.stdin.readline

R1, S = map(int, input().split())
answer = S * 2 - R1
print(answer)