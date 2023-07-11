for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    cnt = 0
    arr = []
    for i in range(0, n):
        line = input()
        # 공백을 지우고 0을 기준으로 나누기
        find_row = line.replace(" ", "").split("0")  # 0 0 1 1 1 -> ['','','111']
        for f_k in find_row:
            # 1이 세개 있으면 cnt + 1
            if len(f_k) == k:
                cnt += 1
        arr.append(line)

    arr2 = list(zip(*arr))
    for line2 in arr2:
        col_find = ''.join(line2)
        col_find = col_find.replace(" ", "").split("0")
        for f_k in col_find:
            if len(f_k) == k:
                cnt += 1
    print(f'#{t} {cnt}')

'''
10
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0
'''
