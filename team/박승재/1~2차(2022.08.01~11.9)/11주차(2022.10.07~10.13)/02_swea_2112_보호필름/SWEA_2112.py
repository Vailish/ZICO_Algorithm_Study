from itertools import combinations


def sol():
    def chk_success(chk_board):
        for i in range(w):
            num = chk_board[0][i]
            cnt = 1
            for j in range(1, d):
                if num != chk_board[j][i]:
                    num = chk_board[j][i]
                    cnt = 1
                else:
                    cnt += 1
                if cnt == k:
                    break
            else:
                return False
        return True

    def chg(s):
        if k == s:
            return s
        for change_list in combinations(range(d), s):
            chk_board = board[:]
            for i in change_list:
                chk_board[i] = [0] * w
            dfs(chk_board, change_list, 0)
            if success:
                return s
        return chg(s + 1)

    def dfs(chk_board, change_list, i):
        nonlocal success
        if success:
            return
        if len(change_list) == i:
            if chk_success(chk_board):
                success = True
            return
        dfs(chk_board, change_list, i + 1)
        dfs(chk_board[:change_list[i]] + [[1] * w] + chk_board[change_list[i]+1:], change_list, i + 1)
        return

    for tc in range(1, int(input()) + 1):
        d, w, k = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(d)]
        if k == 1 or chk_success(board):
            print(f'#{tc} {0}')
            continue
        success = False
        print(f'#{tc} {chg(1)}')


sol()
