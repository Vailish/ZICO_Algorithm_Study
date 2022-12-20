# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PttaaAZIDFAUq

for test_case in range(1,int(input())+1):
    h1, m1, h2, m2 = map(int,input().split())

    m = m1 + m2
    h = h1 + h2
    if m >= 60:
        m -= 60
        h += 1
    if h >= 13:
        h -= 12
    print(f'#{test_case} {h} {m}')