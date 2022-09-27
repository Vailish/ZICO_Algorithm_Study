# 2635. 수 이어가기

n = int(input())

arr = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    result = []
    q = [n, i]
    while True:
        # An = A(n-2) - A(n-1)
        q.insert(2, q[0] - q[1])
        # n이 음수이면 A(n-1)과 A(n-2) 리스트에 더한 후 정지
        if q[2] < 0:
            result += q[:2]
            break
        # A(n-2)는 pop하여 리스트에 추가 q는 한 칸씩 앞으로
        result.append(q.pop(0))
    arr[i] = result
# 최고 길이
ml = max(list(map(len, arr)))
print(ml)
# 가장 긴 케이스
print(*arr[list(map(len, arr)).index(ml)])