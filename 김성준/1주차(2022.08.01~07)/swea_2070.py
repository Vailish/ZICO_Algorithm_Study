#2070. 큰 놈, 작은 놈, 같은 놈 D1
#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE&problemTitle=2070&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

T = int(input())
for case in range(1, T+1):
    A, B = map(int, input().split())
    if A > B:
        print(f'#{case} >')
    elif A < B:
        print(f'#{case} <')
    else:
        print(f'#{case} =')