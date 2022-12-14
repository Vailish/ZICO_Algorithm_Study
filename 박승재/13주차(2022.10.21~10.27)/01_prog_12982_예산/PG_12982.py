def solution(d, budget):
    d.sort()
    answer = 0
    for num in d:
        budget -= num
        if budget < 0:
            break
        answer += 1
    return answer
