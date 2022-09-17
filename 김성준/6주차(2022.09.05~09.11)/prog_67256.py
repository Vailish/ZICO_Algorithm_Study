# 67256 키패드 누르기
# https://school.programmers.co.kr/learn/courses/30/lessons/67256
location = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '7': (2, 0), '8': (2, 1), '9': (2, 2),
    '*': (3, 0), '0': (3, 1), '#': (3, 2)}


def bfs(hand, target):
    visited = [[False] * 3 for _ in range(4)]
    g_x, g_y = location.get(target)
    x, y = location.get(str(hand))
    distance = 0

    if g_x == x and g_y == y:
        return distance
    visited[x][y] = True
    queue = [(x, y, 0)]

    while queue:
        x, y, t = queue.pop(0)
        for i in range(4):
            nx = x + [0, 1, 0, -1][i]
            ny = y + [1, 0, -1, 0][i]

            if nx == g_x and ny == g_y:
                return t

            if 0 <= nx < 4 and 0 <= ny < 3 and not visited[nx][ny]:
                visited[nx][ny] = True
                distance += 1
                queue.append((nx, ny, t + 1))


def solution(numbers, hand):
    lefthand = '*'
    righthand = '#'
    result = ''  # 반환할 값
    for num in numbers:
        if num in [1, 4, 7]:
            lefthand = num
            result += 'L'
        elif num in [3, 6, 9]:
            righthand = num
            result += 'R'
        else:  # num in [2, 5, 8, 0], 가까운손 (같은시에 편한손사용)
            if bfs(lefthand, str(num)) < bfs(righthand, str(num)):  # bfs로 거리계산
                result += 'L'
                lefthand = num
            elif bfs(lefthand, str(num)) > bfs(righthand, str(num)):
                result += 'R'
                righthand = num
            else:  # bfs(lefthand, str(num)) == bfs(righthand, str(num))
                if hand == 'left':
                    result += 'L'
                    lefthand = num
                else:  # hand == 'right'
                    result += 'R'
                    righthand = num
    return result
