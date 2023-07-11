# lst = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
lst = ["SOOOOOL","XOXXOXO","OOOOOOO","OXXOOXX","OOOOEOO"]

len_c = len(lst)
len_r = len(lst[0])

# for i in range(len(lst)):
#     for j in range(len(lst[0])):
#         print(f'i, j = {i}, {j} : {lst[i][j]}')

for i in range(len_c):
    for j in range(len_r):
        print(f'i, j = {i}, {j} : {lst[i][j]}')
