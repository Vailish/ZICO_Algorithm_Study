# def solution(n):
#     answer = 0
#     result = []
#     while n:
#         result.append(n % 3)
#         n //= 3
#     result = result[::-1]
#     for n in range(len(result)):
#         answer += result[n]*(3**n)
#     return answer


def solution(n):
    answer = ''
    while n:
        answer += str(n % 3)
        n //= 3
    print(answer)
    return int(answer, 3)


print(solution(45))
