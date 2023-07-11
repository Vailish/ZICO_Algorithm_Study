# 공 이동 시뮬레이션
# https://school.programmers.co.kr/learn/courses/30/lessons/87391
# 주어진 쿼리값과 같이 이동할 때
# (x,y)에 도착 하는 시작점의 개수를 구해라
# (세로, 가로)
# 거꾸로 해보자
def solution(n, m, x, y, queries):
    min_r, max_r, min_c, max_c = y, y, x, x
    # 거꾸로 돌리면서 범위를 잡아감
    for query in reversed(queries):
        command, dx = query
        if command == 0: # 오른쪽으로감
            max_r += dx
            if max_r > m-1:
                max_r = m-1
            if min_r != 0:
                min_r += dx

        elif command == 1: # 왼쪽으로감
            min_r -= dx
            if min_r < 0:
                min_r = 0
            if max_r != m-1:
                max_r -= dx

        elif command == 2: # 아래쪽으로감
            max_c += dx
            if max_c > n - 1:
                max_c = n - 1
            if min_c != 0:
                min_c += dx

        else: # command == 3일때 # 위쪽으로감
            min_c -= dx
            if min_c < 0:
                min_c = 0
            if max_c != n - 1:
                max_c -= dx

        if min_r > m-1 or max_r < 0 or min_c > n-1 or max_c < 0:
            return 0

    return (max_r - min_r + 1) * (max_c - min_c + 1)


print(solution(2, 2, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]]))
print(solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))
