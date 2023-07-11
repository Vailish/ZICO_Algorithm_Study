def solution(board, moves):
    answer = 0
    N = len(board)
    board2 = [[0]*N for _ in range(N)]
    stack = []
    for i in range(N):
        for j in range(N):
            board2[i][j] = board[j][i]
    for b in board2:
        while b and b[0] == 0:
            b.pop(0)

    for move in moves:
        if board2[move-1]:
            stack.append(board2[move-1].pop(0))
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    return answer


maps = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
m = [1,5,3,5,1,2,1,4]
print(solution(maps,m))


