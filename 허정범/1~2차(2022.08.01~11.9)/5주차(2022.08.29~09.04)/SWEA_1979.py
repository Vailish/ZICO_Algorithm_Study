t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in range(n):
        cnt1 = 0
        cnt2 = 0
        for j in range(n):

            # 가로 탐색
            if puzzle[i][j] == 1:
                cnt1 += 1
            else:
                if cnt1 == k:
                    result += 1
                cnt1 = 0

            # 세로 탐색
            if puzzle[j][i] == 1:
                cnt2 += 1
            else:
                if cnt2 == k:
                    result += 1
                cnt2 = 0

        # 줄이 바뀌기 직전에 확인 (1로 끝나는 경우)
        if cnt1 == k:
            result += 1
        if cnt2 == k:
            result += 1

    print(f"#{tc + 1} {result}")