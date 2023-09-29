# 실버4 - 수 찾기
# https://www.acmicpc.net/problem/1920

# 시간초과
# for와 in으로 10만 * 10만이면 100억이기 때문에 시간초과가 날 수 밖에 없다.(시간제한 1초)
# set을 써보자 (in 연산속도가 list보다 빠르기 때문에)
# list와 tuple은 in 연산자의 시간복잡도가 O(n)
# set과 dict의 경우 시간복잡도가 O(1)이지만, 최악의 경우 O(n) <- hash 충돌이 많아질 경우 성능저하

import sys


sys.stdin = open("input.txt")


N = int(input())
n = set(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

for i in range(M):
    if m[i] in n:
        print(1)
    else:
        print(0)
