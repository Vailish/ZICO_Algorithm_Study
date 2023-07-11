# 1267. [S/W 문제해결 응용] 10일차 - 작업순서
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18TrIqIwUCFAZN

def chk_parent(node):                           # 부모 체크
    if not visited[node]:                       # 방문하지 않은 노드이면
        parents = parent[node]                  # 부모노드 불러오기
        if parents:                             # 부모노드가 있으면
            for p_node in parents:              # 부모노드를 하나씩 p_node에 할당
                chk_parent(p_node)              # p_node들의 부모노드 확인
        result.append(node)                     # 부모노드가 없거나, 부모노드가 모두 방문 완료이면 -> result에 추가
        visited[node] = True                    # 방문 처리



def order(node):                                # 순서 찾기
    if not visited[node]:                       # 방문하지 않은 노드이면
        chk_parent(node)                        # 부모 체크
        for c_node in graph[node]:              # 자식들을 c_node에 할당
            order(c_node)                       # 자식들도 순서 찾기



for t in range(1, 11):
    v, e = map(int, input().split())            # 정점의 개수, 간선의 개수
    edges = list(map(int, input().split()))     # 간선 정보
    graph = [[] for _ in range(v+1)]            # 그래프
    parent = [[] for _ in range(v+1)]           # 부모 정보
    visited = [True] + [False] * v              # 방문 정보
    result = []                                 # 결과를 저장할 리스트
    for i in range(0, e*2, 2):                  # 2씩 건너뛰며 반복
        p, c = edges[i], edges[i+1]             # p : 부모 노드, c : 자식 노드
        graph[p].append(c)                      # 그래프에 정보 저장
        parent[c].append(p)                     # 부모 정보에 저장

    order(1)                                    # 1부터 순서 찾기 시작
    while visited.count(False):                 # 방문하지 않은 노드가 없을 때 까지 반복
        order(visited.index(False))             # 방문하지 않는 노드 순서 찾기 시작
    print(f'#{t}', *result)
