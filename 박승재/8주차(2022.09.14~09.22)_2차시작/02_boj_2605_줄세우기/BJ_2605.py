num = int(input())
move = list(map(int, input().split()))
answer = []
for i in range(1, num+1):
    answer.insert(move[i-1], i)
print(*answer[::-1])
