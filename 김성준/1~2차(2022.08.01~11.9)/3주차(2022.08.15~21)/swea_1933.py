# 1933. 간단한 N 의 약수 D1
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PhcWaAKIDFAUq

N = int(input())
for num in range(N, 0, -1):  # 오름차순이기 때문에 거꾸로
    if N % num == 0:
        print(int(N/num), end=' ')