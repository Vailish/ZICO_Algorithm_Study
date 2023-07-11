w, h = map(int, input().split())

store_num = int(input())
stores = [[] for _ in range(store_num + 1)]

for n in range(store_num + 1):
    i, j = map(int, input().split())
    if i == 1:
        x, y = 0, j
    elif i == 2:
        x, y = h, j
    elif i == 3:
        x, y = j, 0
    else:
        x, y = j, w
    stores[n].extend([i, x, y])

count = 0

for v in range(store_num):
    # if stores[-1][0] + stores[v][0] == 3:
    if (
        stores[-1][0] == 1
        and stores[v][0] == 2
        or stores[-1][0] == 2
        and stores[v][0] == 1
    ):
        w_len = stores[v][2] + stores[-1][2]
        if w_len > w:
            count += w * 2 - w_len + h
        else:
            count += w_len + h
    # elif stores[-1][0] + stores[v][0] == 7:
    elif (
        stores[-1][0] == 3
        and stores[v][0] == 4
        or stores[-1][0] == 4
        and stores[v][0] == 3
    ):
        h_len = stores[v][1] + stores[-1][1]
        if h_len > h:
            count += h * 2 - h_len + w
        else:
            count += h_len + w
    else:
        count += abs(stores[v][1] - stores[-1][1]) + abs(stores[v][2] - stores[-1][2])
print(count)
