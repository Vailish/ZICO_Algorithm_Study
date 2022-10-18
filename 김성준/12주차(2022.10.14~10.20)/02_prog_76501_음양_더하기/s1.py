# programmers 76501 음양 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        answer += absolutes[i] if signs[i] else -absolutes[i]
    return answer
