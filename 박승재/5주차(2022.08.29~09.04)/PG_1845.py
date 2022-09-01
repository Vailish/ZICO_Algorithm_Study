def solution(nums):
    answer = len(nums)//2
    nums = set(nums)
    if len(nums) < answer:
        answer = len(nums)
    return answer


print(solution(list(map(int, input().split()))))
