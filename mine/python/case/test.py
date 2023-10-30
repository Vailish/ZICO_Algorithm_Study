from itertools import combinations


lst = []
for comb in combinations([ i for i in range(5)], 2):
    print(comb)
    lst.append(comb)
print(len(lst))
