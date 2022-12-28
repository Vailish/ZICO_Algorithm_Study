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
    for _ in range(8):                              # 8x8 글자판
        strings = input()                           # 글자 한 줄 받아오기
        board.append(list(map(str, strings)))       # 리스트에 한 글자씩 분리해서 추가
        for idx in range(8 - n + 1):                #
            chk = strings[0+idx:n+idx]              # 문자열 슬라이싱
            chk_reverse(chk)                        # 회문 체크
    reverse_board = list(map(list, zip(*board)))    # 2차원 배열 뒤집기
    for line in reverse_board:                      # 한 줄씩 받아오기
        for idx in range(8 - n + 1):                #
            chk = line[0 + idx:n + idx]             # 리스트 슬라이싱
            chk_reverse(chk)                        # 세로줄 회문 체크
    print(f'#{t} {cnt}')
