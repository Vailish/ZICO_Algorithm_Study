def solution():
    n = int(input())
    texts = [[] for _ in range(51)]
    for _ in range(n):
        chr = input()
        texts[len(chr)].append(chr)
    answer = []
    for chrs in texts[1:]:
        chrs.sort()
    for chrs in texts:
        if chrs:
            for ch in chrs:
                if ch not in answer:
                    answer.append(ch)
    return answer

print('\n'.join(solution()))
