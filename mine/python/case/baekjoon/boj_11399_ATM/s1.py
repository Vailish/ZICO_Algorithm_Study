# ATM - Silver4
# https://www.acmicpc.net/problem/11399

def solution():
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    answer = 0

    for idx, value in enumerate(lst):
        answer += (N-idx) * value

    print(answer)


solution()
