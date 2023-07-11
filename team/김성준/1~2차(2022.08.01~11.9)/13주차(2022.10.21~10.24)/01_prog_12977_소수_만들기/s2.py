def solution(n):
    arr = [[0] * k + [-1] * (n-k) for k in range(1, n+1)]
    r, c = 0, 0
    direction = 0
    arr[r][c] = 1
    for t in range(2, (n * (n+1) //2 )+1):

        # 전진
        nr = r + [1, 0, -1][direction]  # 하 우 좌상
        nc = c + [0, 1, -1][direction]

        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
            arr[nr][nc] = t
            r, c = nr, nc

        else:
            direction = (direction +1) % 3
            nr = r + [1, 0, -1][direction]  # 하 우 좌상
            nc = c + [0, 1, -1][direction]
            arr[nr][nc] = t
            r, c = nr, nc

    # 출력
    result = []
    for num in range(n):
        for num2 in range(n):
            if num >= num2:
                result.append(arr[num][num2])
    return result

print(solution(6))
