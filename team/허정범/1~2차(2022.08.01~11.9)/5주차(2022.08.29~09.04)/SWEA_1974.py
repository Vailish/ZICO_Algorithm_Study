def sudoku(sdk_map):
    # 3 * 3 확인
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            set_a = set()
            for k in range(3):
                for p in range(3):
                    set_a.add(sdk_map[i + k][j + p])
            if len(set_a) != 9:
                return 0

    # 가로 세로 확인
    for i in range(9):
        set_row = set(sdk_map[i])  # 가로
        set_col = set()  # 세로
        for j in range(9):
            set_col.add(sdk_map[j][i])
        if len(set_col) != 9 or len(set_row) != 9:
            return 0

    return 1


t = int(input())
for tc in range(t):
    sdk = [list(map(int, input().split())) for _ in range(9)]
    print(f"#{tc + 1} {sudoku(sdk)}")
