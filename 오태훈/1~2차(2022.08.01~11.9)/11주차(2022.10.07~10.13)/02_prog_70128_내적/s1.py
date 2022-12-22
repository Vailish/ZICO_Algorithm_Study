def solution(a, b):
    # answer = sum(list(map(lambda x: x[0] * x[1], zip(a, b))))
    answer = sum([x * y for x, y in zip(a, b)])
    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))