# 잃어버린 괄호 - silver2
# https://www.acmicpc.net/problem/1541


def solution():
    values = input().split("-")
    result = []
    for value in values:
        tmp = 0
        for nums in value.split("+"):
            tmp += int(nums)
        result.append(tmp)
    answer = result[0]
    for v in range(1, len(result)):
        answer -= result[v]
    print(answer)


solution()
