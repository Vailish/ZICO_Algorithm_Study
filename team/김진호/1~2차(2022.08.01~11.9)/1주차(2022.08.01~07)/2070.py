# 2070 큰놈,작은놈,같은놈
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
