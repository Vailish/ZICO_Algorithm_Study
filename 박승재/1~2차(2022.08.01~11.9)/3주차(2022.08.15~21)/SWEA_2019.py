# for i in range(int(input()) + 1):
#     print(2**i, end=' ')


def square(n):
    if n:
        square_list.append(square(n - 1) * 2)
    return square_list[n]


square_list = [1]
square(int(input()))
print(*square_list)
