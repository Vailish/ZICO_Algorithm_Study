# 직사각형 네개의 합집합의 면적 구하기 브론즈1
# https://www.acmicpc.net/problem/2669

# import sys
# sys.stdin = open('input.txt')

field = [[0] * 100 for _ in range(100)]
for _ in range(4):
    # 좌표평면에서 n1, n2 왼쪽 하단 좌표, n3, n4 우측 상단 좌표
    n1, n2, n3, n4 = map(int, input().split())

    # 위 아래만 다른 이중리스트로 좌표를 변경시켜 주면
    a1 = n2
    a2 = n1
    b1 = n4
    b2 = n3

    for i in range(a1, b1):
        for j in range(a2, b2):
            field[i][j] = 1
result = 0
for lst in field:
    result += sum(lst)
print(result)
