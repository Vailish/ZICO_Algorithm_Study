# 실버4 - 수 찾기
# https://www.acmicpc.net/problem/1920

# 시간초과
import sys


sys.stdin = open("input.txt")


N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

for i in range(N):
    if n[i] in m:
        print(1)
    else:
        print(0)
