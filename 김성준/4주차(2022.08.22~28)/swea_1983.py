# 1983. 조교의 성적 매기기 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PwGK6AcIDFAUq

for case in range(1, 1 + int(input())):
    N, K = map(int, input().split())  # N = 학생수, K = 학생번호
    score = [list(map(int, input().split())) for _ in range(N)]
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    score_sort = []

    for num, sc1, sc2, sc3 in enumerate(score):
        score_sort.append([num, ((sc1 * 0.35 + sc2 * 0.45 + sc3 * 0.2)/3)])  # [[0, 20] [1, 30]]
        score_sort = sorted(score_sort, key=lambda x: x[1], reverse=True)

    for n in score_sort:
        if K == n[0]:
            result = K//(N//len(grades))
            print(result, K)
            # K는 1~10만 되야함
            # N이 10을 넘길 수있음
            print(f'#{case} {grades[result+1]}')
