def dfs(t, result):
    global answer
    if result >= answer:
        return
    if t > 11 and answer > result:
        answer = result
        return
    dfs(t+1, result + plan[t])
    dfs(t+3, result + m_3)


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=' ')
    d, m, m_3, y = map(int, input().split())
    plan = list(map(int, input().split()))
    answer = y
    for i in range(12):
        if plan[i] > 0:
            if plan[i] * d >= m:
                plan[i] = m
            else:
                plan[i] *= d
    dfs(0, 0)
    print(answer)
