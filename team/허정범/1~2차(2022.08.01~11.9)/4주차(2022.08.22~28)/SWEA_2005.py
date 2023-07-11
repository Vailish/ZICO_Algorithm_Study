def pascal(n):
    if len(memo) >= n:
        return memo[0:n]
    else:
        add_line = [1]
        for i in range(n - 2):
            add_line.append(pascal(n - 1)[-1][i] + pascal(n - 1)[-1][i + 1])
        add_line.append(1)
        memo.append(add_line)
        return memo[0:n]


memo = [[1]]
t = int(input())
for tc in range(t):
    n = int(input())
    print(f"#{tc + 1}")
    for j in pascal(n):
        print(*j)
