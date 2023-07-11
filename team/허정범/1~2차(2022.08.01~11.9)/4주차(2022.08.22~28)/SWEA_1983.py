t = int(input())
for tc in range(t):
    grade_list = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    n, k = map(int, input().split())
    score_list = []
    for i in range(n):
        a, b, c = map(int, input().split())
        sum_value = a * 0.35 + b * 0.45 + c * 0.2
        score_list.append(sum_value)
    sorted_list = sorted(score_list, reverse=True)
    idx = sorted_list.index(score_list[k - 1])
    print(f"#{tc + 1} {grade_list[idx // (n // 10)]}")