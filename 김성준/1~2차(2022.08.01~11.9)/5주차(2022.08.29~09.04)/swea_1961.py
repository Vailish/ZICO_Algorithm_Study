# 1961. 숫자 배열 회전 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq

for case in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_90 = ''
    arr_180 = ''
    arr_270 = ''
    # 첫 행 구하기
    for i in range(N):
        for j in range(N):
            arr_90 += str(arr[-j-1][i])
            arr_180 += str(arr[-i-1][-j-1])
            arr_270 += str(arr[-j-1][i])
    for num in range(N):
        print(arr_90[N * num -N : N * num - 1], arr_180[N * num -N : N * num - 1], arr_270[N * num -N : N * num - 1])
