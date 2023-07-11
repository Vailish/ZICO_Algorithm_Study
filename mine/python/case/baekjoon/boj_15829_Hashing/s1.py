def solution():
    N = int(input())
    alpha = input()
    result = 0
    for i in range(N):
        result += (ord(alpha[i])-96) * (31 ** i)
    return result % 1234567891


print(solution())
