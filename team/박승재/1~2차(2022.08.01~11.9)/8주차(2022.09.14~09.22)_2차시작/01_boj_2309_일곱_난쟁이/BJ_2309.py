from itertools import combinations


h = [int(input()) for i in range(9)]
for comb in list(combinations(h, 7)):
    if sum(comb) == 100:
        print(*sorted(list(comb)), sep="\n")
        break


