# 최소 힙 - silver2
# https://www.acmicpc.net/problem/1927
import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    heap = [0]*100001
    last = 0

    def enq(x):
        nonlocal last
        last += 1
        heap[last] = x
        c = last
        p = last//2
        while p and heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            c = p
            p = c//2

    def deq():
        nonlocal last
        tmp = heap[1]
        heap[1] = heap[last]
        last -= 1
        p = 1
        c = p * 2
        while c <= last:
            if c+1 <= last and heap[c] > heap[c+1]:
                c += 1
            if heap[c] < heap[p]:
                heap[c], heap[p] = heap[p], heap[c]
                p = c
                c = p * 2
            else:
                break
        return tmp


    for _ in range(n):
        n = int(input())
        if (n==0):
            if last > 0:
                print(deq())
            else:
                print(0)
        else:
            enq(n)


solution()
