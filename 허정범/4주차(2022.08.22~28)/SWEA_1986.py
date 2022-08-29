t = int(input())
for tc in range(t):
    n = int(input())

    result = (n + 1) // 2 * ((-1) ** (n + 1) % 2)

    # result = 0
    # for j in range(1, n + 1):
    #     if j % 2 == 0:
    #         result -= j
    #     else:
    #         result += j

    print(f"#{tc + 1} {result}")
