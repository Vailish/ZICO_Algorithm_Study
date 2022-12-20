x, y = map(int, input().split())
board = [[0, y], [0, x]]  # 인덱스 0일 때 세로길이 변화 인덱스 1일 때 가로길이 변화
n = int(input())
m_x, m_y = 0, 0
for _ in range(n):
    t, p = map(int, input().split())
    board[t].append(p)
board[0].sort()
board[1].sort()
for i in range(len(board[0]) - 1):
    temp = board[0][i + 1] - board[0][i]
    if temp > m_x:
        m_x = temp
for j in range(len(board[1]) - 1):
    temp = board[1][j + 1] - board[1][j]
    if temp > m_y:
        m_y = temp
print(m_x * m_y)