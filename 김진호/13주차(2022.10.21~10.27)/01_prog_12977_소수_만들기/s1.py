from itertools import *

def solution(nums):
    subset_lists = list(combinations(nums, 3))
    cnt = 0
    for subset in subset_lists:
        temp = sum(subset)
        is_sosu = True
        for num in range(2,temp//2+1):
            if temp % num == 0:
                is_sosu = False
                break
        if is_sosu:
            cnt += 1

    return cnt