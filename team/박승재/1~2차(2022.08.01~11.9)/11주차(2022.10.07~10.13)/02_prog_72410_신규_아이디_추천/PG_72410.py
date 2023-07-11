def solution(new_id):
    def chk_bool(w):
        return w in chk or w.isalpha() or w.isdecimal()

    answer = ''
    chk = {'-', '_', '.'}
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for word in new_id:
        if chk_bool(word):
            answer += word
    # 3단계
    while answer.count('..'):
        answer = answer.replace('..', '.')
    # 4단계 처음만
    if answer[0] == '.':
        answer = answer[1:]
    # 5단계
    if not answer:
        answer += 'a'
    # 6단계 처음
    if len(answer) > 15:
        answer = answer[:15]
    # 4, 6단계 마지막
    if answer[-1] == '.':
        answer = answer[:-1]
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]
    return answer


print(solution(input()))
