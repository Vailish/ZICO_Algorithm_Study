
dice = []
chk = [0, 6, 4, 5, 2, 3, 1]
n = int(input())
for _ in range(n):
    dice.append([0] + list(map(int, input().split())))
answer = 0
for i in range(1, 7):
    p = i
    result = 0
    for j in range(n):
        b = dice[j][chk.index(dice[j].index(p))]
        result += max(set(chk)-set([p, b]))
        p = b
    if answer < result:
        answer = result
print(answer)



