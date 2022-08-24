t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            cnt = 0
            for row in range(m):
                for col in range(m):
                    cnt += total_map[i + row][j + col]

            if max_cnt < cnt:
                max_cnt = cnt

    print(f"#{tc + 1} {max_cnt}")


# # 슬라이딩 윈도우를 사용하고 싶었지만 가로방향으로만 사용 세로까지 생각하려니 머리아파요..ㅠㅠ
# t = int(input())
# for tc in range(t):
#     n, m = map(int, input().split())
#     total_map = [list(map(int, input().split())) for _ in range(n)]
#     max_cnt = 0
#     for i in range(n - m + 1):
#         cnt = 0
#         for row in range(m):
#             for col in range(m):
#                 cnt += total_map[i + row][col]
#         if max_cnt < cnt:
#             max_cnt = cnt

#         for j in range(1, n - m + 1):
#             for k in range(m):
#                 cnt -= total_map[i + k][j - 1]
#                 cnt += total_map[i + k][j + m - 1]
#             if max_cnt < cnt:
#                 max_cnt = cnt

#     print(f"#{tc + 1} {max_cnt}")
