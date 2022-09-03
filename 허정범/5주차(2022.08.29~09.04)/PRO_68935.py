def solution(n):
    if n < 3:
        return n

    answer = ""
    while n >= 3:
        answer += str(n % 3)
        n //= 3
    answer += str(n)

    return int(answer, 3)
