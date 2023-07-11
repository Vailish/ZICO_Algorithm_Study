# 1986. 지그재그 숫자

for t in range(1, int(input()) + 1):
    N = int(input())
    result = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            result -= i
        else:
            result += i
    print(f'#{t} {result}')
