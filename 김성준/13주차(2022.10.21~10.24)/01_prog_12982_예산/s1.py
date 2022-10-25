# 12982 예산
# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    answer = 0
    for num in range(len(d)):
        if budget >= d[num]:
            budget -= d[num]
            answer += 1
        else:
            return answer
    return answer
