def solution():
    A, B, V = map(int, input().split())
    result, r = divmod(V-B, A-B)
    return result if not r else result + 1


print(solution())