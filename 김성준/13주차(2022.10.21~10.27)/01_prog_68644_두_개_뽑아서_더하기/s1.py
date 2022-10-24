# prog_68644 두 개 뽑아서 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    result = []
    n = len(numbers)
    for i in range(n-1):
        for j in range(i+1, n):
            num = numbers[i] + numbers[j]
            if num not in result:
                result.append(num)
    result.sort()
    return result
