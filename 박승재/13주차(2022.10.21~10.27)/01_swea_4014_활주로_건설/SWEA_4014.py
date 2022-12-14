def sol():
    def chk(li):
        ck = [0] * n
        for k in range(n):
            left = k - 1
            right = k + 1
            if 0 <= left < n and li[k] > li[left]:
                if not 0 <= k - x < n or abs(li[k] - li[left]) != 1:
                    return 0
                for s in range(x):
                    ck[left - s] += 1
            if 0 <= right < n and li[k] > li[right]:
                if not 0 <= k + x < n or abs(li[k] - li[right]) != 1:
                    return 0
                for s in range(x):
                    ck[right + s] += 1
        for k in range(n):
            if ck[k] > 1:
                return 0
        return 1

    for tc in range(1, int(input()) + 1):
        n, x = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        answer = 0
        for i in range(n):
            col = []
            for j in range(n):
                col.append(board[j][i])
            answer += chk(board[i]) + chk(col)
        print('#{} {}'.format(tc, answer))


sol()
