alph_str = input()

for alph in alph_str:
    print(ord(alph) - 64, end=' ')


'''
# ord 미사용

alph_str = input()
alph_list = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
]

for alph in alph_str:
    for idx in range(26):
        if alph == alph_list[idx]:
            print(idx + 1, end=' ')

'''
