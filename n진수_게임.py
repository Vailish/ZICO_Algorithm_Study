# # [3차] n진수 게임
# # https://school.programmers.co.kr/learn/courses/30/lessons/17687
#
# # 문제이슈
#
# # n진법 변환 함수
# def change_number(number, n):
#     if number == 0:
#         return '0'
#
#     rev_base = ''
#
#     while number > 0:
#         number, mod = divmod(number, n)
#         # 11진법 이상일 시 A ~ F로 변경
#         if mod >= 10:
#             mod = ['A', 'B', 'C', 'D', 'E', 'F'][mod % 10]
#         rev_base += str(mod)
#
#     return rev_base[::-1]
#
#
# # 문제풀이 메인 함수
# def solution(n, t, m, p):
#     # 1) n진법으로해서 문자열로 쭉 이어 붙인다
#     tmp_number = ''
#     for num in range(m*t):
#         tmp_number += change_number(num, n)
#
#     # 2) 그 다음 튜브의 순서만 뽑아서 이어붙인다
#     answer = ''
#     cnt = 0
#     print(tmp_number)  # n = 2, t = 4까지, 인원 2명, 내순서 1
#     # 원래는 0 1 10 11
#     # for value in tmp_number:
#     #     cnt += 1
#     #     if cnt == p:
#     #         answer += value
#     #     if cnt == m:
#     #         cnt = 0
#     for i in range(t):
#         answer += tmp_number[p - 1 + m * i]
#
#     return answer
#
#
# print('답', solution(2, 4, 2, 1))
# print('답', solution(16, 16, 2, 1))
# print('답', solution(16, 16, 2, 2))
#
# '''
# alpha = ['','A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#
# def solution(msg):
#     mydict = alpha
#     answer = []
#     i = 0
#     while i < len(msg):
#         tempword = msg[i]
#         j = i
#
#         while 1:
#             j += 1
#             if j == len(msg):
#                 searchword = tempword
#                 answer.append(mydict.index(searchword))
#                 break
#
#             tempword += msg[j]
#             if tempword not in mydict:
#                 newword = tempword
#                 searchword = tempword[:-1]
#                 mydict.append(newword)
#                 answer.append(mydict.index(searchword))
#                 break
#
#         i = j
#     return answer
# '''

def solution(m, musicinfos):
    answer = '(None)'
    t = 0
    for i in range(len(musicinfos)):
        start, end, name, song = musicinfos[i].split(',')
        time = 60 * (int(end[:2]) - int(start[:2])) + int(end[3:5]) - int(start[3:5])
        print(time, 'time')

        if 'C#' in song:
            for num in range(len(song)):
                if song[num] == '#':
                    song[num] = '!'

        # C#, D#, F#, G#, A#

        if time > t:
            result = ''
            n = 0
            cnt = time
            while cnt > 0:
                result += song[n]
                if song[n] != '#':
                    cnt -= 1
                n = (n + 1) % len(song)
            if song[n] == '#':
                result += '#'
            print(result, 'result')
            if m in result and m + '#' not in result:
                answer = name
                t = time
    print(answer, 'answer')
    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
