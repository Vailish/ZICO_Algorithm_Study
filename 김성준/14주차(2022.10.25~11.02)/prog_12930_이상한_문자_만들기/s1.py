# prog_12930 이상한_문자_만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    # chara = list(s.split())  # 여백이 두 개면, 두개다 출력하길 원하는 문제인듯..
    # split()와 split(' ')의 차이는 모든 ' ' 와 하나의 ' '만 제거한다는 차이가 있음
    chara = list(s.split(' '))
    result = []
    for chr in chara:
        tmp = ''
        for n in range(len(chr)):
            if not n % 2:  # 나머지가 1, 짝수번
                tmp += chr[n].upper()
            else:
                tmp += chr[n].lower()
        result.append(tmp)
    return ' '.join(result)


print(solution("   TRY            hello         world         "))
