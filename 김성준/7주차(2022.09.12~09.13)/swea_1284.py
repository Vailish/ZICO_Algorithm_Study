# 1284. 수도 요금 경쟁 D2 Attack
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV189xUaI8UCFAZN

for case in range(1, 1+int(input())):
    p, q, r, s, w = map(int,input().split())

    a = p * w
    if w <= r:
        b = q
    else:
        b = q + s * (w - r)

    if a >= b:
        print(f'#{case} {b}')
    else:
        print(f'#{case} {a}')
