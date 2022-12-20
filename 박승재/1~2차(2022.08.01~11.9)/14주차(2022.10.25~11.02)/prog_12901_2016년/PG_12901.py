def solution(a, b):
    return ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'][
        (sum([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][: a - 1]) + b) % 7
    ]
