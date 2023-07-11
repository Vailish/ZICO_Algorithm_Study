def solution(maps):
    answer = 100000
    # dfs
    def dfs(start, end, depth, visited):
        nonlocal answer

        start_i, start_j = start

        # 방문처리
        visited[start_i][start_j] = 1

        # 도착했을 때
        if start == end:
            answer = min(depth, answer)
            return

        if depth > len(maps[0]) * len(maps):
            return

        # 델타이동
        #      상 하 좌 우
        # dr = [0, 0, -1, 1]
        # dc = [-1, 1, 0, 0]
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr, nc = start_i + dr, start_j + dc

            if 0 < nr < len(visited) and 0 < nc < len(visited[0]) and maps[nr][nc] != "X":
                dfs((nr, nc), end, depth + 1, visited)

        return

    # 초기 변수 설정하기 시작지점, 출구, 레버 설정하기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":    # 시작지점
                start_point = (i, j)
            elif maps[i][j] == "E":  # 종료지점
                end_point = (i, j)
            elif maps[i][j] == "L":  # 레버위치
                lever = (i, j)

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]


    dfs(start_point, lever, 0, visited)  # 시작지점에서 레버위치까지 이동

    dfs(lever, end_point, 0, visited)    # 레버위치에서 도착지점까지 이동

    if a

    return to_lever + to_exit

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) # 답 16
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) # 답 -1