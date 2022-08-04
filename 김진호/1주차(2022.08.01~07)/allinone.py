# 20220802_2071 평균값 구하기
# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

# 문제 풀이 고려사항
# 1. 10개의 수라는 입력받는 개수 지정
# 2. 소수점 첫째자리에서 반올림한 '정수'값 (round())
# 3. 코드를 짧게보다는 한단계씩 진행하도록

# test input
'''
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   
'''
# test output
'''
#1 24
#2 29
#3 27
# '''

T = int(input())

for test_case in range(1, T + 1):
    num10_list = list(map(int, input().split()))
    num10_sum = sum(num10_list)
    num10_avg = round(num10_sum / 10)

    print(f'#{test_case} {num10_avg}')

'''eval 함수
for T in range(int(input())):
    sum = eval(input().replace(" ", "+"))
    avg = int(round(sum / 10))
    print(f'#{T} {avg}')
'''


# 20220803_2070 큰놈,작은놈,같은놈
# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

# 문제 풀이 고려사항
# 1. 입력은 공백을 한칸둔 2개의 수
# 2. < = > 3가지로 표현
# 3. 코드를 짧게보다는 한단계씩 진행하도록

# test input
'''
3
3 8 
7 7 
369 123  
'''
# test output
'''
#1 <
#2 =
#3 >
# '''

T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    if A == B:
        print(f'#{test_case} =')
    elif A > B:
        print(f'#{test_case} >')
    else:
        print(f'#{test_case} <')
