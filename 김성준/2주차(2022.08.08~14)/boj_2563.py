# 색종이 브론즈1
#https://www.acmicpc.net/problem/2563

papers = int(input())

# 이중리스트를 생성한다.
# 이중리스트 끼리 더한다.
# 그러면 2이상만 골라서 세어주면 된다.
field = [[0]*100 for _ in range(100)]
A = [[0]*100 for _ in range(100)]
B = [[0]*100 for _ in range(100)]
C = [[0]*100 for _ in range(100)]

# A, B, C 생성
ai, aj = map(int, input().split())
bi, bj = map(int, input().split())
ci, cj = map(int, input().split())

for i in range(ai, ai+10):
    for j in range(ai, ai+10):
        A[i][j] = 1
for i in range(bi, bi+10):
    for j in range(bi, bi+10):
        B[i][j] = 1
for i in range(ci, ci+10):
    for j in range(ci, ci+10):
        C[i][j] = 1        

for i in range(len(field)):
    for j in range(len(field)):
        field[i][j] = A[i][j] + B[i][j] + C[i][j]

counts_2 = 0
counts_3 = 0
for i in range(len(field)):
    for j in range(len(field)):
        if field[i][j] == 2:
            counts_2 += 1
        elif field[i][j] == 3:
            counts_3 += 1
print(100*papers -counts_2 - counts_3)