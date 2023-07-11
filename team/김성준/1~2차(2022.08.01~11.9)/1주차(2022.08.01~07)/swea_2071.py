#2071. 평균값 구하기 D1
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1&&&&&&&&&&

T = int(input())

for case in range(1, T+1):
    test_case = list(map(int,input().split()))
    print(f'#{case} {round(sum(test_case)/len(test_case))}')