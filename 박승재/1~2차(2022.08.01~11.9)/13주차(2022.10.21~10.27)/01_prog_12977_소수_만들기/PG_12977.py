def solution(nums):
    nums = list(set(nums))
    nums.sort()
    sum_num = nums[-1] + nums[-2] + nums[-3]
    num_chk = set()
    chk = [True] * 2 + [False] * (sum(nums) - 1)
    for i in range(2, sum_num + 1):
        if not chk[i]:
            num_chk.add(i)
            for j in range(2 * i, sum_num + 1, i):
                chk[j] = True
    answer = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] in num_chk:
                    answer += 1
    return answer
