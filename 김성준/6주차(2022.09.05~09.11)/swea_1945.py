# 1945. 간단한 소인수분해 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pl0Q6ANQDFAUq

def solution(num):
    N = num
    result = [0] * 5  # 순서대로 a, b, c, d, e
    numbers = [2, 3, 5, 7, 11]  # 소수

    # 제일 큰 수부터 나눠서
    i = 0
    while True:
        if i > 4:
            return result
        else:
            a, b = divmod(N, numbers[i])  # a = 몫, b = 나머지
            if b == 0:
                result[i] += 1
                N = a
            else:
                i += 1


for case in range(1, 1 + int(input())):
    answer = solution(int(input()))
    print(f'#{case}', end=" ")
    print(*answer)
