# 디펜스 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/142085

from heapq import heappush, heappop


def solution(n, k, enemy):
    # 힙 안으로 넣어서 k번 이후부터 제일 작은 수들만 병사 값에서 빼주면 됨!
    heap = []
    for idx in range(len(enemy)):
        heappush(heap, enemy[idx])
        if idx + 1 > k:
            n -= heappop(heap)
        if n < 0:
            return idx
    return len(enemy)

# 아래는 초기 풀이(틀린풀이) - DFS(깊이 우선탐색)로 풀기
# 시간초과... 혹은 깊이 오류...

# def solution(n, k, enemy):
#     stage = 0
#
#     def dfs(t, n, k):
#         nonlocal stage
#         # 가지치기
#         if t == len(enemy):
#             stage = len(enemy)
#             return
#
#         # 최고값 갱신해주기
#         if stage < t:
#             stage = t
#
#         # 병사 사용하기
#         if n >= enemy[t]:
#             dfs(t + 1, n - enemy[t], k)
#
#         # 턴넘기기 사용하기
#         if k > 0:
#             dfs(t + 1, n, k - 1)
#
#     # n = 병사 수
#     # k = 턴넘기기 수
#     # enemy = 적 병사수
#     # dfs(턴, 남은 병사수, 남은 k)로 풀자
#
#     dfs(0, n, k)
#
#     return stage
#
#
# print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
# print(solution(2, 4, [3, 3, 3, 3]))
