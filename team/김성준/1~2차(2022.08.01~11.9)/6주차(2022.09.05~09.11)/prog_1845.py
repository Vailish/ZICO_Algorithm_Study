# 1845. 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3

def solution(nums):
    ponketmon = nums[:]
    n = len(ponketmon)/2
    answer = 0
    if len(set(ponketmon)) >= n:
        return n
    else:
        return len(set(ponketmon))