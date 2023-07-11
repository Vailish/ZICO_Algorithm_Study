def solution(n):
    answer = 0
    result = []
    while n:
        result.append(n % 3)
        n //= 3
    result = result[::-1]
    for n in range(len(result)):
        answer += result[n]*(3**n)
    return answer