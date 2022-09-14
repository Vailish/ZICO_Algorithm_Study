# 1946. 간단한 압축 풀기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PmkDKAOMDFAUq
for tc in range(1, int(input()) + 1):
    N = input()
    t = ''
    for j in range(0, int(N)):
        x = str(input()).split()
        t += x[0] * int(x[1])
        L = len(t)
    print('#' + str(tc))
    for k in range(1, L // 10 + 2):
        print(t[slice(k * 10 - 10, k * 10)])
