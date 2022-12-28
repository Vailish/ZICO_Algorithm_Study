def solution(participant, completion):
    # completion.append('zzzzzzz')
    for x, y in zip(sorted(participant), sorted(completion)):
        if x != y:
            return x
    return sorted(participant)[-1]
