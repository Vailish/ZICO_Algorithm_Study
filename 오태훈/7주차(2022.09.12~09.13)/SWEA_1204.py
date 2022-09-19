# 1204. 최빈수 구하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh

for t in range(1, int(input()) + 1):
    input()
    nums = {}
    arr = map(int, input().split())

    for num in arr:
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 0
    print(f'#{t} {sorted(nums, key=lambda x: nums[x], reverse=True)[0]}')

    # arr = list(map(int, input().split()))
    # r = max(arr, key=arr.count)
    # print(f'#{t} {r}')
