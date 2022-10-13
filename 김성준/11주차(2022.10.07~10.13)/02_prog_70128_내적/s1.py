# 내적
# https://school.programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i]*b[i]
    return result


# def solution(a, b):
#
#     return sum([x*y for x, y in zip(a,b)])