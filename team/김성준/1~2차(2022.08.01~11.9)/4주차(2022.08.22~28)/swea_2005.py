# 2005. 파스칼의 삼각형 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq
T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    for i in range(0, N):
        arr[i][0] = 1
        for j in range(1, N):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        print(*arr[i][0:i+1])