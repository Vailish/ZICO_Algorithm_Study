# 1946. 간단한 압축 풀기 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PmkDKAOMDFAUq

for case in range(1, 1+int(input())):
    N = int(input())
    chars = ''
    stack = []
    for _ in range(N):
        lst = input()
        lst.replace("10", "!")
        stack.append(lst)

    cnt = 0
    print(f'#{case}')
    for char in range(len(chars)):
        cnt += 1
        print(char)
        if cnt == 10:
            print()
            cnt = 0

