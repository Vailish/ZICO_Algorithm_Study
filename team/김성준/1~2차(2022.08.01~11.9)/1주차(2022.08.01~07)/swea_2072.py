#2072. 홀수만 더하기 D1
#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=2072&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

T = int(input())

for case in range(1, T+1):
    test_case = list(map(int,input().split()))
    sum_list =  []
    for num in test_case:
        if num %2 :
            sum_list.append(num)
    print(f'#{case} {sum(sum_list)}')