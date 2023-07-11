t = int(input())
for tc in range(t):
    n = int(input())
    matrix = [list(input().split()) for _ in range(n)]
    result = [[] for _ in range(n)]
    for _ in range(3):
        matrix = list(zip(*matrix[::-1]))
        for i in range(n):
            result[i].append("".join(matrix[i]))

    print(f"#{tc + 1}")
    for j in range(n):
        print(*result[j])
