# 슬라이딩 윈도우 추가. 재귀검색 사용
# 아래 오른쪽 탐색
import time
import sys

start = time.process_time()
sys.stdin = open("input.txt")
T = int(input())


def fly(x,y,total):
    global fly_sum_max
    if 0 <= x+1 < N-M+1 and 0 <= y < N-M+1 and not(visit[x+1][y]):
        new_total = total
        visit[x+1][y] = True
        for j in range(M):
            new_total -= fly_map[x][y+j]
            new_total += fly_map[x+M][y+j]
        if fly_sum_max < new_total:
            fly_sum_max = new_total
        fly(x+1,y,new_total)

    if 0 <= x < N - M +1 and 0 <= y+1 < N - M +1 and not visit[x][y+1]:
        new_total = total
        visit[x][y + 1] = True
        for i in range(M):
            new_total -= fly_map[x+i][y]
            new_total += fly_map[x+i][y+M]
        if fly_sum_max < new_total:
            fly_sum_max = new_total
        fly(x,y+1,new_total)

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    visit = [[False] * (N-M+1) for _ in range(N-M+1)]
    fly_map = [list(map(int, input().split())) for _ in range(N)]
    sum_count = 0
    fly_sum_max = 0

    for i in range(M):
        for j in range(M):
            sum_count += fly_map[i][j]  # 첫 영역만 구하기
    if fly_sum_max < sum_count:
        fly_sum_max = sum_count
    fly(0,0,sum_count)
    print(f'#{test_case} {fly_sum_max}')

end = time.process_time()
print("Time elapsed: ", end - start)  # seconds