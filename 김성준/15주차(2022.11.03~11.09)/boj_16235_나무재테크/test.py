arr = [[[]] for _ in range(3) for _ in range(3)]
brr = [[[1]], [[2]], [[3]], [[4]], [[5]], [[]]]
crr = [[[1, 2, 3], [2], [3, 8, 0], [4]],
       [[1, 2, 3], [8, 2, 3], [4, 2, 3], [5, 5, 5]]]

drr = [[[1] for _ in range(3)] for _ in range(3)]
err = drr[:]
print(err==drr)
print(drr)
'''
[[[]], [[]], [[]]]
[[[]], [[]], [[]]]
[[[]], [[]], [[]]]
'''
# print(arr)
# arr[3][3].append(5)
# print(arr)
# arr[0]