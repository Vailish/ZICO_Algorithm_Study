# 4466. 최대 성적표 만들기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWOUfCJ6qVMDFAWg

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    print(f'#{t} {sum(scores[:k])}')
