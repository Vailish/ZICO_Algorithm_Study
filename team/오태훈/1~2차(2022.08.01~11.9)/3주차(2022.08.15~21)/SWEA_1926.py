# 1926. 간단한 369게임

N = int(input())

for i in range(1, N + 1):
    # 문자열 변환
    i = str(i)
    cnt = 0
    # n자리 수일 때 한 자리씩 3,6,9인지 검사
    for j in i:
        if j == '3' or j == '6' or j == '9':
            cnt += 1
    if cnt > 0:
        i = '-' * cnt
    print(i, end=" ")
