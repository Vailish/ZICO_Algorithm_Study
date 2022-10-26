def solution(d, budget):
    d.sort()
    total = 0
    answer = 0
    for i,k in enumerate(d,1):
        if total + k <= budget:
            total += k
            answer += 1
        else:
            break
    return answer