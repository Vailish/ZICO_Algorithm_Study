# 듣보잡 - Silver4
# https://www.acmicpc.net/problem/1764

def solution():
    N, M = map(int, input().split())
    my_dict = dict()
    answer = []

    for _ in range(N):
        my_dict[input().strip()] = 1

    for _ in range(M):
        target = input().strip()
        if target in my_dict:
            answer.append(target)
    answer.sort()
    print(len(answer))
    for value in answer:
        print(value)


solution()
