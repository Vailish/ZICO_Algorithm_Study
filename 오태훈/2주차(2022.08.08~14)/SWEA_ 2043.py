# 2043. 서랍의 비밀번호
P, K = map(int, input().split())

if P > K:  # P가 K보다 큰 경우
    print(P - K + 1)
else:  # P가 K보다 작은 경우
    print(999 - K + P + 1)
