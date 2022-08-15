# 1926. 간단한 369게임

N = int(input())

for i in range(1, N + 1):
    i = str(i)
    cnt = 0
    for j in i:
        if j == '3' or j == '6' or j == '9':
            cnt += 1
        else:
            pass
    if cnt > 0:
        i = '-' * cnt
    print(i, end=" ")
