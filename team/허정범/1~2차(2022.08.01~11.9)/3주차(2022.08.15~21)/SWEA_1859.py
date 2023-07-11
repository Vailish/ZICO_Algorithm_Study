t = int(input())
for tc in range(t):
    n = int(input())
    num_list = list(map(int, input().split()))

    cnt = 0
    sell_idx = n - 1
    for i in range(n - 2, -1, -1):
        if num_list[i] <= num_list[sell_idx]:
            cnt += num_list[sell_idx] - num_list[i]
        else:
            sell_idx = i
    print(f"#{tc + 1} {cnt}")
