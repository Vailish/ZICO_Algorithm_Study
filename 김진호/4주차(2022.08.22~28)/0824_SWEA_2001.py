# 파리퇴치
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq
import time
import sys
from datetime import timedelta

start = time.process_time()
sys.stdin = open("input.txt")
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    fly_map = [list(map(int, input().split())) for _ in range(N)]
    sum_count = 0
    fly_sum_max = 0
    x_idx = 0
    y_idx = 0
    while not(sum_count == (N-M+1)**2):         # 종료조건. 영역을 구하는 횟수에 도달하면 반복 멈춤
        fly_sum = 0
        for i in range(x_idx, x_idx + M):
            for j in range(y_idx, y_idx + M):
                fly_sum += fly_map[i][j]        # 영역합 구하기(좌측상단에서 M*M만큼)

        if fly_sum_max < fly_sum:
            fly_sum_max = fly_sum               # 최대값 갱신

        y_idx += 1
        if y_idx == N-M+1:
            y_idx = 0
            x_idx += 1                          # 영역합을 시작할 좌측상단 위치 구하기

        sum_count += 1                          # 영역합을 구한 횟수 + 1

    print(f'#{test_case} {fly_sum_max}')

end = time.process_time()
print("Time elapsed: ", end - start)  # seconds