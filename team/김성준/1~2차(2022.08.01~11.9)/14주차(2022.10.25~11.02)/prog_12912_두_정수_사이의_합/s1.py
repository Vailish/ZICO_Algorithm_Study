# prog_12912 나누어 떨어지는 숫자 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    a, b = sorted((a, b))
    answer = 0
    for num in range(a, b+1):
        answer += num
    return answer