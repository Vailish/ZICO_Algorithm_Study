# 1845. 폰켓몬


def solution(nums):
    set_nums = set(nums)
    num = len(set_nums)
    n_2 = len(nums) // 2
    if num > n_2:
        result = n_2
    else:
        result = num
    return result


def solution(nums):
    # return len(nums) // 2 if len(set(nums)) > len(nums) // 2 else len(set(nums))
    return min([len(set(nums)), len(nums)])
