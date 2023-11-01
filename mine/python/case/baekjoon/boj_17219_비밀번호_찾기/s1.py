import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline


def solution():
    my_dict = dict()
    N, M = map(int, input().split())
    for _ in range(N):
        address, password = input().split()
        my_dict[address] = password

    for _ in range(M):
        print(my_dict[input()])


solution()
