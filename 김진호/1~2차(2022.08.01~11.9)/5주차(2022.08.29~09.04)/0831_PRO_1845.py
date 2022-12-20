# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    result = len(set(nums))
    if result > len(nums) // 2:
        result = len(nums) // 2
    return result