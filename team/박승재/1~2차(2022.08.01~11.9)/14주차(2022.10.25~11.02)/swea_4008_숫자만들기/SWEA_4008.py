def sol():
    def calculator(n1, n2, o):
        if o == 0:
            return n1 + n2
        if o == 1:
            return n1 - n2
        if o == 2:
            return n1 * n2
        if o == 3:
            return int(n1 / n2)

    def dfs(num, op, a):
        nonlocal max_num, min_num
        if a == n:
            if max_num < num:
                max_num = num
            if min_num > num:
                min_num = num
            return
        for i in range(4):
            if op[i] > 0:
                op[i] -= 1
                dfs(calculator(num, nums[a], i), op[:], a + 1)
                op[i] += 1

        return

    for tc in range(1, int(input()) + 1):
        n = int(input())
        operator = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        min_num = 10**10
        max_num = -1 * min_num
        dfs(nums[0], operator, 1)
        print('#{} {}'.format(tc, max_num - min_num))


sol()
