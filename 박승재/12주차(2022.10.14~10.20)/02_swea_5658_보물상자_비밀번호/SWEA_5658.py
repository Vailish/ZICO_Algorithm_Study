def sol():
    for tc in range(1, int(input()) + 1):
        n, k = map(int, input().split())
        num = input()
        nums = set()
        n //= 4
        for _ in range(n):
            nums.update((num[:n], num[n : 2 * n], num[2 * n : 3 * n], num[3 * n :]))
            num = num[-1] + num[:-1]
        nums = sorted(list(nums))[::-1]
        print('#{} {}'.format(tc, int(nums[k - 1], 16)))


sol()
