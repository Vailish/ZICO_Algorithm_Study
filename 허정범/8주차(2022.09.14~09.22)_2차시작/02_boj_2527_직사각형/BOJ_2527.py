def sol(arr):
    if arr[4] > arr[2] or arr[5] > arr[3] or arr[6] < arr[0] or arr[7] < arr[1]:
        return 'd'
    elif arr[0] == arr[6] or arr[2] == arr[4]:
        if arr[1] == arr[7] or arr[3] == arr[5]:
            return 'c'
        else:
            return 'b'
    elif arr[1] == arr[7] or arr[3] == arr[5]:
        return 'b'
    else:
        return 'a'


for _ in range(4):
    arr = list(map(int, input().split()))
    print(sol(arr))
