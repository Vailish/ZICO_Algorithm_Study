# 64061. 크레인 인형뽑기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/64061


def solution(board, moves):
    r_board = list(map(list, zip(*board)))
    l = len(r_board[0])
    box = []
    cnt = 0
    for i, b in enumerate(r_board):
        while 0 in b:
            r_board[i].pop(b.index(0))
    for t in moves:
        if r_board[t - 1]:
            s = r_board[t - 1].pop(0)
            if box and box[-1] == s:
                box.pop()
                cnt += 2
            else:
                box.append(s)

    return cnt


def solution(board, moves):
    # 0 지우기
    r_board = list(
        map(
            lambda x: (' ' + '  '.join(map(str, x)) + ' ')
            .replace(' 0 ', '')
            .replace(' ', ''),
            zip(*board),
        )
    )
    # 문자열 다시 뒤집어서 리스트로 만들기
    r_board = list(map(lambda x: list(map(int, x))[::-1], r_board))
    print(r_board)
    box = []
    cnt = 0
    for t in moves:
        if r_board[t - 1]:  # [0,0,0,0] -> []
            s = r_board[t - 1].pop()
            if box and box[-1] == s:
                box.pop()
                cnt += 2
            else:
                box.append(s)

    return cnt


print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4],
    )
)
