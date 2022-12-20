# 1984. 중간 평균값 구하기 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pw_-KAdcDFAUq

for case in range(1, 1 + int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.pop()
    arr.pop(0)
    print(f'#{case} {round(sum(arr)/len(arr))}')
