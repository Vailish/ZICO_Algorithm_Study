# 색종이 만들기 - silver2
# https://www.acmicpc.net/problem/2630


def soultion():
    def chk(r, c, l):
        nonlocal cnt_w, cnt_b
        state = paper[r][c]
        for i in range(r, r + l):
            for j in range(c, c + l):
                if paper[i][j] != state:
                    chk(r, c, l//2)
                    chk(r+l//2, c, l//2)
                    chk(r, c+l//2, l//2)
                    chk(r+l//2, c+l//2, l//2)
                    return
        if state == 0:
            cnt_w += 1
        else:
            cnt_b += 1

    n = int(input())
    cnt_w, cnt_b = 0, 0
    paper = []
    for _ in range(n):
        paper.append(list(map(int, input().split())))
    chk(0, 0, n)

    print(cnt_w)
    print(cnt_b)


soultion()
