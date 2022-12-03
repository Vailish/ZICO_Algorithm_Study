def solution(left, right):
    return sum([-i if round(i**0.5) ** 2 == i else i for i in range(left, right + 1)])
