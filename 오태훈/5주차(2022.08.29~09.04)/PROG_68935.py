# 3진법 뒤집기


def solution(n):
    ternary = ''
    while n != 0:
        ternary += str(n % 3)
        n = n // 3
    return int(ternary, 3)


print(solution(125))
