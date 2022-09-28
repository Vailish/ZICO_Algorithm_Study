def chk(nums):
    while True:
        if nums[-2] < nums[-1]:
            return nums
        nums.append(nums[-2] - nums[-1])


# 46368/75025
n = int(input())
answer = []
for num in range(int(n * 0.61), int(n * 0.62) + 2):
    chk_nums = chk([n, num])
    if len(answer) < len(chk_nums):
        answer = chk_nums
print(len(answer))
print(*answer)

n = int(input())
answer = []
for num in range(n // 2, n + 1):
    chk_nums = chk([n, num])
    if len(answer) < len(chk_nums):
        answer = chk_nums
print(len(answer))
print(*answer)
