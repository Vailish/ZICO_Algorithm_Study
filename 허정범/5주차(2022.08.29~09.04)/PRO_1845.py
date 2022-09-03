def solution(nums):
    answer = 0
    n = len(nums) // 2
    if len(set(nums)) < n:
        answer = len(set(nums))
    else:
        answer = n
    return answer
