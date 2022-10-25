# 하 우 좌상 하 우 좌상
di = [1, 0, -1]
dj = [0, 1, -1]


def solution(n):
    def dfs(i, j, direction):
        nonlocal count
        count += 1
        visited[i][j] = True
        arr[i][j] = count

        next_i = i + di[direction]
        next_j = j + dj[direction]
        if 0 <= next_i < n and 0 <= next_j < n and not visited[next_i][next_j]:
            count += 1
            visited[next_i][next_j] = True
            arr[next_i][next_j] = count

            for _ in range((n * (n + 1)) // 2):
                next_i += di[direction]
                next_j += dj[direction]
                print(next_i, next_j)
                print(arr)

                if 0 <= next_i < n and 0 <= next_j < n and not visited[next_i][next_j]:
                    count += 1
                    visited[next_i][next_j] = True
                    arr[next_i][next_j] = count
                else:
                    direction = (direction + 1) % 3


    arr = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    count = 0
    dfs(0, 0, direction=0)
    answer = arr
    return answer


# print(solution(4))
print(solution(5))
# print(solution(6))