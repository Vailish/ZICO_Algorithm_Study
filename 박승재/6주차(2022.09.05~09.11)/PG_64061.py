def solution(board, moves):
    answer = 0
    length = len(board)
    queue = []

    for move in moves:
        for i in range(length):
            if board[i][move-1] != 0:
                if queue and queue[-1] == board[i][move-1]:
                    queue.pop()
                    answer += 2
                else:
                    queue.append(board[i][move-1])
                board[i][move - 1] = 0
                break

    return answer

