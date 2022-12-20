# def solution(N, stages):
#     result = []
#     answer = []
#     chk = set(stages)
#     stages = sorted(stages)[::-1]
#     people = 0
#     n = N
#     cnt = 0
#     for stage in stages:
#         people += 1
#         if stage == n:
#             cnt += 1
#         elif stage < n:
#             if cnt != 0 and people > 1:
#                 answer.append((n, cnt/(people-1)))
#             n = stage
#             cnt = 1
#     else:
#         if cnt != 0:
#             answer.append((n, cnt/people))
#     answer.sort(key=lambda x: x[1], reverse=False)
#     print(answer)
#     for ans in range(len(answer)-1, -1, -1):
#         result.append(answer[ans][0])
#         chk.add(answer[ans][0])
#     for i in range(1, N + 1):
#         if i not in chk:
#             result.append(i)
#     return result


def solution(N, stages):
    result = list(range(N, 0, -1))
    answer = []
    stages = sorted(stages)[::-1]
    people = 0
    n = N
    cnt = 0
    for stage in stages:
        people += 1
        if stage == n:
            cnt += 1
        elif stage < n:
            if cnt != 0 and people > 1:
                answer.append((n, cnt/(people-1)))
            n = stage
            cnt = 1
    else:
        if cnt != 0:
            answer.append((n, cnt/people))
    answer.sort(key=lambda x: x[1], reverse=False)
    for ans in answer:
        i = ans[0]
        del result[result.index(i)]
        result.append(i)
    return result[::-1]


stages = [2, 1, 2, 6, 2, 4, 3, 3]
stages = sorted(stages)[::-1]
print(solution(5, stages))
# print(stages)