# 1로 만들기 - silver 3
# https://www.acmicpc.net/problem/1463


def solution():
    answer = 10 ** 10

    def dfs(num, cnt):
        nonlocal answer

        if cnt >= answer:
            return

        if num == 1:
            if answer > cnt:
                answer = cnt
            return

        if num % 3 == 0:
            dfs(num / 3, cnt + 1)
        if num % 2 == 0:
            dfs(num / 2, cnt + 1)
        dfs(num - 1, cnt + 1)

    dfs(int(input()), 0)
    print(answer)


solution()

'''
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
10 -> 9 -> 3 -> 1
'''