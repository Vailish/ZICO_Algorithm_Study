# 5431. 민석이의 과제 체크하기 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl3rWKDBYDFAXm

import sys
sys.stdin = open('input.txt')


def solution():
    students = list(range(1, N+1))  # 전체 학생 번호 생성
    for num in complited_student:   # 제출 학생 번호 제거
        students.remove(num)
    return students


for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N = 수강 인원, M = 제출 인원
    complited_student = list(map(int, input().split()))
    print(f'#{case}', *solution())
