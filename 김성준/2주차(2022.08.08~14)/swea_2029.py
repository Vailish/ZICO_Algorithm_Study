# 2029. 몫과 나머지 출력하기 D1
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QGNvKAtEDFAUq

for case in range(1, 1 + int(input())):
    a, b = map(int,input().split())
    print(f'#{case} {a//b} {a%b}')