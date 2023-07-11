# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PnnU6AOsDFAUq

# 1. 각달 날짜 활용 연산

days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def sol(m1,d1,m2,d2):
    result = d2 - d1 + 1
    for i in range(m1,m2):
        result += days[i]
    return result

for test_case in range(1,int(input())+1):
    print(f'#{test_case} {sol(*map(int,input().split()))}')

# 2. date 함수 활용

from datetime import date

for test_case in range(1,int(input())+1):
    m1,d1,m2,d2 = map(int, input().split())
    result = date(1,m2,d2) - date(1,m1,d1)
    print(f'#{test_case} {result.days+1}')