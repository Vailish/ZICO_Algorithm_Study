# 1986. 지그재그 숫자 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PxmBqAe8DFAUq

# print(f'#{case}',[((-1)**i) * int(i + 1 // 2) for i in range(1, 1 + int(input()))] for case in range(1, 1 + int(input()))], sep="\n")
#
# print()

for case in range(1, 1+int(input())):
    [(-1)**i * int(i + 1 // 2) for i in range(1, 1 + int(input()))]
    a=1