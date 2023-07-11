# 공 이동 시뮬레이션
# https://school.programmers.co.kr/learn/courses/30/lessons/87391
# 주어진 쿼리값과 같이 이동할 때
# (x,y)에 도착 하는 시작점의 개수를 구해라
# (세로, 가로)
# 시간초과
def solution(n, m, x, y, queries):
    def function(start, end):
        r, c = start, end
        for query in queries:
            tmp = 0
            while tmp < query[1]:
                nr = r + [0, 0, -1, 1][query[0]]
                nc = c + [-1, 1, 0, 0][query[0]]
                if 0 <= nr < n and 0 <= nc < m:
                    r, c = nr, nc
                tmp += 1
        if (r, c) == (x, y):
            return True
        else:
            return False

    result = 0

    for i in range(n):
        for j in range(m):
            result += function(i, j)
    return result