# 1979. 어디에 단어가 들어갈 수 있을까 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq

# for case in range(1, 1 + int(input())):
#     N, K = map(int, input().split())  # N = 퍼즐 길이, K = 단어 길이
#     puzzle = [list(map(int, input().split())) for _ in range(N)]
#     lst = []
#     for i in range(N):
#         for j in range(N - K + 1):
#             cnt_1 = 0  # 가로검사
#             cnt_2 = 0  # 세로검사
#             for num in range(j, K):
#                 if puzzle[i][num]:
#                     cnt_1 += 1
#                 if puzzle[num][i]:
#                     cnt_2 += 1
#             lst.append(cnt_1)
#             lst.append(cnt_2)
#             print(lst)
#     print(f'#{case} {lst.count(K)}')


for case in range(1, 1 + int(input())):
    N, K = map(int, input().split())  # N = 퍼즐 길이, K = 단어 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        temp_1 = 0
        temp_2 = 0
        for j in range(N):
            if puzzle[i][j]:
                temp_1 += 1
            else:
                result.append(temp_1)
                temp_1 = 0

            if puzzle[j][i]:
                temp_2 += 1
            else:
                result.append(temp_2)
                temp_2 = 0


        if temp_1 != 0:
            result.append(temp_1)
        if temp_2 != 0:
            result.append(temp_2)

    print(f'#{case} {result.count(K)}')
