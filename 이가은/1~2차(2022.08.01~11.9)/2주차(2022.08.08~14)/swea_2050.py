alphabets = input()
num_list = []

for i in alphabets:
    num = ord(i) - 64
    num_list.append(str(num))

print(' '.join(num_list))
