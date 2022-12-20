import sys

sys.stdin = open("input.txt")


def turn(number, direction):
    if direction == 1:
        board[number] = [board[number][-1]] + board[number][:-1]
        return
    board[number] = board[number][1:] + [board[number][0]]


def chk_turn_dfs(location, direction, way):
    if location in break_option or board[location][-2 * direction] == board[location - direction][2 * direction]:
        return
    chk_turn_dfs(location + direction, direction, -way)
    turn(location, way)


break_option = (-1, 4)
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=' ')
    k = int(input())
    board = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(k):
        num, d = map(int, input().split())
        chk_turn_dfs(num - 2, -1, -d)
        chk_turn_dfs(num, 1, -d)
        turn(num - 1, d)
    print(1 * board[0][0] + 2 * board[1][0] + 4 * board[2][0] + 8 * board[3][0])
