def solution(s):
    answer = ''
    ind = 0
    for i in range(len(s)):
        if s[i] == ' ':
            ind = -1
            w = ' '
        elif ind % 2 == 0:
            w = s[i].upper()
        elif ind % 2 == 1:
            w = s[i].lower()
        answer += w
        ind += 1
    return answer
