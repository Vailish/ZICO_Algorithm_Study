# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq

T = int(input())

for test_case in range(1, T + 1):
    sdouq = [list(map(int, input().split())) for _ in range(9)]

    # # 1_1 가로 세로 zip 사용 검증 (곱셈)
    # val = True
    # for _ in range(2):
    #     for row in sdouq:
    #         check = 1
    #         for n in row:
    #             check *= n
    #         if check != 362880:
    #             val = False
    #     sdouq = list(map(list, zip(*sdouq)))
    #
    # # 2_1 3*3 사이즈 검증(곱셈)
    # for i_start in range(0, 9, 3):
    #     for j_start in range(0, 9, 3):
    #         chk = 1
    #         for i in range(i_start, i_start + 3):
    #             for j in range(j_start, j_start + 3):
    #                 chk *= sdouq[i][j]
    #         if chk != 362880:
    #             val = False

    # 1_2 입력값이 무조건 1~9이고, 스도쿠의 검증은 9개가 다 달라야하므로, set을 통해 검증
    val = True
    for _ in range(2):
        for idx in range(9):
            if len(set(sdouq[idx])) != 9:
                val = False
        sdouq = list(map(list, zip(*sdouq)))

    # 2_2 3*3 사이즈 검증(set)
    for i_start in range(0, 9, 3):
        for j_start in range(0, 9, 3):
            chk = set()
            for i in range(i_start, i_start + 3):
                for j in range(j_start, j_start + 3):
                    chk.add(sdouq[i][j])
            if len(set(chk)) != 9:
                val = False
    #
    # # 3_1 가로,세로,3*3 한번에 검증
    # val = True
    # chk = [[1] * 3 for _ in range(3)]
    # for i in range(9):
    #     chk_i = 1
    #     chk_j = 1
    #     for j in range(9):
    #         chk_i *= sdouq[i][j]                # 가로 검증
    #         chk_j *= sdouq[j][i]                # 세로 검증
    #         chk[i//3][j//3] *= sdouq[i][j]      # 3*3씩 검증 [0][0] ~ [2][2]까지 생성됨
    #     if chk_i != 362880 or chk_j != 362880:
    #         val = False
    #
    # for i in range(3):
    #     for j in range(3):
    #         if chk[i][j] != 362880:
    #             val = False

    print(f'#{test_case} {int(val)}')