# 1215. [S/W 문제해결 기본] 3일차 - 회문1
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi

def chk_reverse(s):
    global cnt
    if s == s[::-1]:
        cnt += 1

for t in range(1, 11):
    n = int(input())
    board = []
    cnt = 0
    for _ in range(8):
        strings = input()
        board.append(list(map(str, strings)))
        for idx in range(8 - n + 1):
            chk = strings[0+idx:n+idx]
            chk_reverse(chk)
    reverse_board = list(map(list, zip(*board)))
    for line in reverse_board:
        for idx in range(8 - n + 1):
            chk = line[0 + idx:n + idx]
            chk_reverse(chk)
    print(f'#{t} {cnt}')
