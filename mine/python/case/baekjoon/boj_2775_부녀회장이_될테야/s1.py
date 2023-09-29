# 브론즈1 - 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775


# 0층의 각 k호에는 호수에 맞는 n명이 산다
# 0층 1  2  3  4  5  6  7  8  9 10 11 12 13 14
# 1층 1 3 6 10 14 19
# 2층 1 4 9 16 26 40
# 미리 계산한 후에 구해주면 될거 같음

def solution():
    apartment = [[0] * 14 for _ in range(15)]  # 0층도 포함하기 때문
    # 아파트 주민 수 채우기
    # 0층
    for j in range(14):
        apartment[0][j] = j + 1
    # 나머지층
    for i in range(1, 15):
        for j in range(14):
            tmp = 0
            for k in range(j+1):
                tmp += apartment[i-1][k]
            apartment[i][j] = tmp

    for _ in range(int(input())):
        k = int(input())
        n = int(input())
        print(apartment[k][n-1])


solution()
