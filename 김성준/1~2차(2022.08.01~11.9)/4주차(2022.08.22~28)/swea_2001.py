# 2001. 파리 퇴치 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq

for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N = 필드, M = 파리채의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    kills = []
    # 파리잡기
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_kill = 0
            # 파리채의 범위
            for a in range(i, i + M):
                for b in range(j, j + M):
                    sum_kill += arr[a][b]
            kills.append(sum_kill)

    print(f'#{case} {max(kills)}')
