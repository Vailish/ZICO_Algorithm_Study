for t in range(1, int(input()) + 1):
    m = int(input())
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    result = [0] * 8

    for j, i in enumerate(arr):
        cnt = 0
        while i <= m:
            m -= i
            cnt += 1
        result[j] = cnt
    print(f'#{t}')
    print(*result)
