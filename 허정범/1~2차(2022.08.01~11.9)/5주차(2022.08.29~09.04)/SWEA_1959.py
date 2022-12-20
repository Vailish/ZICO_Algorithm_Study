t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    sum_list = []

    if n >= m:
        for i in range(n - m + 1):
            sum_value = 0
            for j in range(m):
                sum_value += list_a[i + j] * list_b[j]
            sum_list.append(sum_value)
    else:
        for i in range(m - n + 1):
            sum_value = 0
            for j in range(n):
                sum_value += list_b[i + j] * list_a[j]
            sum_list.append(sum_value)

    print(f"#{tc + 1} {max(sum_list)}")
