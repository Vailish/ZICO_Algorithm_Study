# 최대 힙 - silver2
# https://acmicpc.net/problem/11279
import heapq, sys
input = sys.stdin.readline


def solution():
    n = int(input())
    heap = []
    answer = ""
    for _ in range(n):
        k = int(input())
        if k == 0:
            answer += str(-heapq.heappop(heap) if heap else 0) + "\n"
        else:
            heapq.heappush(heap, -k)
    print(answer)


solution()
