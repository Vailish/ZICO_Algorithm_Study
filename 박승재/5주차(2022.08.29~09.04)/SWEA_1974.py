def sodocu(sodocu_list):
    check_list = list(range(1, 10))
    sodocu_list_col = list(zip(*sodocu_list))
    #  행, 열 정렬이 check_list와 다를 경우 0 반환
    for i in range(9):
        if sorted(sodocu_list[i]) != check_list or sorted(sodocu_list_col[i]) != check_list:
            return 0
    #  3x3 list가 check_list와 다를 경우 0 반환
    for i in range(3):
        for j in range(3):
            check_list_33 = []
            for x in range(3):
                for y in range(3):
                    check_list_33.append(sodocu_list[i * 3 + x][j * 3 + y])
            if sorted(check_list_33) != check_list:
                return 0
    #  다 통과하면 1 반환
    return 1


T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    sodocu_list = [list(map(int, input().split())) for _ in range(9)]

    print(sodocu(sodocu_list))


