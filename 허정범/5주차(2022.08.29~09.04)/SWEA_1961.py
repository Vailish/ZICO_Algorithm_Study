def turn(list_a):
    result = list(map(list, zip(*list_a)))
    for i in range(n):
        result[i] = "".join(result[i])[::-1]
    return result


t = int(input())
for tc in range(t):
    n = int(input())
    list_a = [list(input().split()) for _ in range(n)]
    arr1 = turn(list_a)
    arr2 = turn(arr1)
    arr3 = turn(arr2)

    print(f"#{tc + 1}")
    for i in range(n):
        print(arr1[i], arr2[i], arr3[i])
