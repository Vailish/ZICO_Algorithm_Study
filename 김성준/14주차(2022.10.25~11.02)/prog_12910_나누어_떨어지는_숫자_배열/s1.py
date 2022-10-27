# prog_12910 나누어 떨어지는 숫자 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    for num in sorted(arr):
        if not num % divisor:
            answer.append(num)
    if not answer:
        answer = [-1]
    return answer