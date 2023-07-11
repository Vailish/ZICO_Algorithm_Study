def solution():
    A, B = map(int, input().split())
    a = max(A, B)
    b = min(A, B)

    # 최대 공약수
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            print(i)
            break

    # 최소 공배수
    for j in range(1, a*b +1):
        if j % a == 0 and j % b == 0:
            print(j)
            break


solution()
