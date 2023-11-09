# 피보나치 함수 - silver 3
# https://www.acmicpc.net/problem/1003

def solution():
    n = int(input())
    zeros = [1, 0, 1]
    ones = [0, 1, 1]

    def func(k):
        if k >= len(zeros):
            for i in range(len(zeros), k+1):
                zeros.append(zeros[i-1] + zeros[i-2])
                ones.append(ones[i-1] + ones[i-2])

    for _ in range(n):
        num = int(input())
        func(num)
        print(f'{zeros[num]} {ones[num]}')


solution()
