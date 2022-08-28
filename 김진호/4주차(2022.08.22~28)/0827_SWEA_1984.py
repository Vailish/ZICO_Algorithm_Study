for test_case in range(1,int(input())+1):
    nums = list(map(int, input().split()))
    nums.sort()
    result = round(sum(nums[1:9]) / 8)
    print(f'#{test_case} {result}')