# 2491. 수열
# https://www.acmicpc.net/problem/2491

n = int(input())
nums = list(map(int, input().split()))

cnt, e_cnt = 1, 1
arr = []
status = 0
for idx, num in enumerate(nums[:-1]):
    if num < nums[idx + 1]:
        if status != 1:
            status = 1
            arr.append(cnt)
            cnt = e_cnt
        e_cnt = 1
    elif num > nums[idx + 1]:
        if status != -1:
            status = -1
            arr.append(cnt)
            cnt = e_cnt
        e_cnt = 1
    else:
        e_cnt += 1
    cnt += 1
arr.append(cnt)
if not arr:
    result = n
else:
    result = max(arr)
print(result)
