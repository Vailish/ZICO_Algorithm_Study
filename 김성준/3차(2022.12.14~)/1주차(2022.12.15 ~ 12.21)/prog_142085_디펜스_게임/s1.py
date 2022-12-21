# 디펜스 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/142085

#####################################################################################
# heap(min)의 특성은 새로운 녀석이 들어오면 구조상 제일 앞에 최소값을 배치하게 된다.#
# 이를 이용하면 문제를 쉽게 해결할 수 있다.                                         #
# 1. 무적권을 사용할 수 있는 k번째까지 heap안에 넣어준다.                           #
# (이제 이 안에 있는 녀석들은 전부 무적권을 사용할 녀석들이다.)                     #
# 2. 다음 번 녀석을 집어 넣으면, 자동으로 그 안에서 최소인 녀석이 나온다.           #
# (최소인 녀석을 제외하고 나머지 녀석들이 무적권 사용 대상이다.)                    #
# 3. 그 녀석을 heappop을 이용해서 빼서 병사 수에서 제거한다.                        #
# 4. 이를 반복해서 병사가 음수가 되었을 때, 그 때의 라운드를 출력하면 된다.         #
# 5. 만약 전부 통과했다면, 최종 라운드를 출력하면 된다.                             #
#####################################################################################


from heapq import heappush, heappop


def solution(n, k, enemy):
    # 힙 안으로 넣어서 k번 이후부터 제일 작은 수들만 병사 값에서 빼주면 됨!
    heap = []
    for idx in range(len(enemy)):
        heappush(heap, enemy[idx])
        if idx + 1 > k:             # range가 0부터 시작하므로 idx + 1
            n -= heappop(heap)      
        if n < 0:
            return idx
    return len(enemy)

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))

# 아래는 초기 풀이(틀린풀이) - DFS(깊이 우선탐색)로 풀기
# 시간초과... 혹은 깊이 오류...
# 제한사항이 아래와 같으므로 사용 불가
# 1 ≤ n ≤ 1,000,000,000
# 1 ≤ k ≤ 500,000
# 1 ≤ enemy의 길이 ≤ 1,000,000
# 1 ≤ enemy[i] ≤ 1,000,000

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
