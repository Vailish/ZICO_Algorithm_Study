lst = [1, 1, 1, 2, 3, 4, 2, 3, 1, 5, 6]

print(lst)

from collections import Counter

my_lst = Counter(lst)
print(my_lst)

my_lst2 = my_lst.most_common() # 최빈값순으로 정렬하는데, 내림차순 순으로 정렬해줌
print(my_lst2)
print(my_lst2[0][1])