# solved.ac - 실버4
# https://www.acmicpc.net/problem/18110

import sys


sys.stdin = open("input.txt")
# sys.stdin = open("input2.txt")


def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


def solution():
    n = int(input())
    if n == 0:
        return 0
    rates = []
    for _ in range(n):
        rates.append(int(input()))
    k = my_round(n * 0.15)
    return my_round(sum(sorted(rates)[k:-k]) / (n - 2 * k)) if k != 0 else my_round(sum(sorted(rates)) / n)


print(solution())
