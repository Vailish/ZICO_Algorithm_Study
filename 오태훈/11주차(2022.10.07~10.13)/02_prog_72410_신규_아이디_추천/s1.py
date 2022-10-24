def solution(new_id):
    exception = {'-', '_', '.'}
    id_1 = new_id.lower()
    id_2 = ''
    for i in id_1:
        if i.islower() or i.isnumeric() or i in exception:
            id_2 += i
    id_3 = id_2
    while '..' in id_3:
        id_3 = id_3.replace('..', '.')

    while True:
        if id_3 and id_3[0] == '.':         # strip('.')
            id_3 = id_3[1:]
        elif id_3 and id_3[-1] == '.':
            id_3 = id_3[:-1]
        else:
            id_4 = id_3
            break

    if not id_4:
        id_5 = 'a'
    else:
        id_5 = id_4

    if len(id_5) >= 16:
        id_6 = id_5[:15]
        if id_6[-1] == '.':
            id_6 = id_6[:-1]
    else:
        id_6 = id_5

    if len(id_6) <= 2:
        while len(id_6) < 3:
            id_6 += id_6[-1]
    id_7 = id_6
    return id_7

print(solution(	"abcdefghijklmn.p"))