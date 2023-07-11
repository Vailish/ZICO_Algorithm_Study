def sol():
    N, K = map(int, input().split())
    grade = []
    for _ in range(N):
        m, f, h = map(int, input().split())
        grade.append((m*0.35)+(f*0.45)+(h*0.20))
    K = grade[K-1]
    grade.sort(reverse=True)
    print(result[(grade.index(K))//(N//10)])


T = int(input())
result = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')
    sol()
