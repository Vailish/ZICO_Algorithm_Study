# lv2 점 찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/140107

# def solution(k, d):
#     result = []
#     for a in range(d+1):
#         for b in range(d+1):
#             if (a*k)**2 + (b*k)**2 <= d**2:
#                 result.append((a*k, b*k))
#     return len(result)

# print(solution(2, 4))
# print(solution(1, 5))


def solution(k, d):
    result = []
    b = d//2
    for a in range(d+1):
        if a + b <= d//k:
            pass

    return len(result)


print(solution(2, 4))
print(solution(1, 5))

