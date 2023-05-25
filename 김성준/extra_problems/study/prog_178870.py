def solution(sequence, k):
    answer = []
    if k in sequence:
        return [sequence.index(k), sequence.index(k)]

    for size in range(2, len(sequence)):
        # 기본 값 = 0부터 size-1 까지의 합

        for i in range(len(sequence) - size + 1):
            if i == 0:
                value = sum(sequence[0:size])
            else:
                # i번째일 때, i부터 i + size-1을 더 해야함
                value = value + sequence[i + size - 1] - sequence[i -1]
            if value == k:
                return [i, i + size -1]

    return answer

# print(solution([1, 2, 3, 4, 5], 7))
# print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))
