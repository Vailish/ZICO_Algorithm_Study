my_map = [list(map(int, input().split())) for _ in range(5)]
sol_map = []
for _ in range(5):
    for i in map(int, input().split()):
        sol_map.append(i)

for idx in range(25):
    bg_cnt = 0
    host_num = sol_map[idx]

    for j in range(5):
        breaker = False
        for k in range(5):
            if my_map[j][k] == host_num:
                my_map[j][k] = 0
                breaker = True
                break
        if breaker:
            break

    cross_sum = 0
    reverse_cross_sum = 0
    for cross_idx in range(5):
        cross_sum += my_map[cross_idx][cross_idx]
        reverse_cross_sum += my_map[cross_idx][4 - cross_idx]
    if cross_sum == 0:
        bg_cnt += 1
    if reverse_cross_sum == 0:
        bg_cnt += 1

    for check_line in my_map:
        if sum(check_line) == 0:
            bg_cnt += 1

    new_my_map = list(map(list, zip(*my_map)))
    for check_line in new_my_map:
        if sum(check_line) == 0:
            bg_cnt += 1

    if bg_cnt >= 3:
        print(idx + 1)
        break
