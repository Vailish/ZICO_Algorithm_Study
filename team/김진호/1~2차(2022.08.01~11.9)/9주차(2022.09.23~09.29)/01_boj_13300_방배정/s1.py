import sys
sys.stdin = open("input.txt")

N, K = map(int,input().split())
students = [[0,0] for _ in range(6)]
result = 0
for _ in range(N):
    S, Y = map(int,input().split())
    students[Y-1][S] += 1
for F, M in students:
    if F:
        result += F // K + 1
        if F % K == 0:
            result -= 1
    if M:
        result += M // K + 1
        if M % K == 0:
            result -= 1
print(result)



print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()
