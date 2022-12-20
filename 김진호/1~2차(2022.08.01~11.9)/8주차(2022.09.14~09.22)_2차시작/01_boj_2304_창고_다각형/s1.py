import sys
sys.stdin = open("input.txt")

N = int(input())
boxes = [list(map(int,input().split())) for _ in range(N)]
boxes.sort(key=lambda x:x[0])
max_height = max(b[1] for b in boxes)
result = 0
right_end, left_end = boxes[0][0], boxes[N-1][0]
before_height = boxes[0][1]
before_idx = boxes[0][0]
for idx in range(0,N):
    if boxes[idx][1] >= before_height:
        result += before_height * (boxes[idx][0] - before_idx)
        before_height = boxes[idx][1]
        before_idx = boxes[idx][0]
    if before_height == max_height:
        result += max_height
        left_end = before_idx
        break


before_height = boxes[N-1][1]
before_idx = boxes[N-1][0]
for idx in range(N-1,0,-1):
    if boxes[idx][1] >= before_height:
        result += before_height * (before_idx - boxes[idx][0])
        before_height = boxes[idx][1]
        before_idx = boxes[idx][0]

    if before_height == max_height:
        right_end = before_idx
        break

result += (right_end - left_end) * max_height

print(result)

print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()
