# 1959. 두 개의 숫자열 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq

for case in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    if len(Ai) >= len(Bj):
        lst = Bj[:]
        Bj = Ai[:]
        Ai = lst[:]
    temp = 0
    result = []
    for n in range(len(Bj) - len(Ai) + 1):  # 3, 2 이면 -> range(2)
        for num in range(len(Ai)):  # 2이면 0, 1
            temp += Bj[n + num] * Ai[num]
        result.append(temp)
        temp = 0
    print(f'#{case} {max(result)}')
