#2056. 연월일 달력 D1
#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=2056&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

T = int(input())

check = {1:'31', 2:'28', 3:'31', 4:'30', 5:'31', 6:'30', 7:'31', 8:'31', 9:'30', 10:'31', 11:'30', 12:'31'}
for case in range(1, T+1):
    date = input()
    if 13 > int(date[4:6]) > 0: #월 오입 제거
        if int(date[6:8]) <= int(check.get(int(date[4:6]))): # 입력 일일과 확인표 최대 일일 비교 
            print(f'#{case} {date[0:4]}/{date[4:6]}/{date[6:8]}')
        else:
            print(f'#{case} -1')
    else:
        print(f'#{case} -1')
