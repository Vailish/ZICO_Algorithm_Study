def solution(numbers):
    answer = set()
    N = len(numbers)
    for i in range(N-1):
        for j in range(i+1,N):
            answer.add(numbers[i]+numbers[j])
    answer = sorted(list(answer))
    return answer