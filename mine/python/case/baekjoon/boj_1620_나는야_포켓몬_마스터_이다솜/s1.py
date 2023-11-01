# 나는야 포켓몬 마스터 이다솜 - Silver4
# https://www.acmicpc.net/problem/1620
# 시간초과
def solution():
    N, M = map(int, input().split())
    lst = []
    for _ in range(N):
        lst.append(input())

    for i in range(M):
        target = input()
        if target.isdigit():
            print(lst[int(target)-1])
        else:
            print(lst.index(target)+1)


solution()
