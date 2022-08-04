#swea_2072 (D1)

T = int(input())
for test_case in range(1, T + 1):
    sum = 0
    nums = list(map(int,input().split()))
    for num in nums:
        if num % 2 == 1:
            sum += num
    print(f'#{test_case} {sum}')