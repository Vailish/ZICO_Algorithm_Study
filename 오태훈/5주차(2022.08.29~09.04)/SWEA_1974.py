# 1974. 스도쿠 검증

# 검사 함수 (집합 자료형 사용)
def chk(arr):
    if len(set(arr)) == 9:
        return 1
    return 0


for t in range(1, int(input()) + 1):
    # 스도쿠 입력 받기
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    # 행 검사하기
    sudoku_chk = 0 if 0 in set(map(chk, sudoku)) else 1
    # 행 에러
    if not sudoku_chk:
        print(f'#{t} {0}')
        continue
    # 열 검사
    reverse_chk = 0 if 0 in set(map(chk, zip(*sudoku))) else 1
    # 열 에러
    if not reverse_chk:
        print(f'#{t} {0}')
        continue
    # 3x3 박스 만들기
    box = []
    for row in range(0, 7, 3):
        for col in range(0, 7, 3):
            box.append(
                sudoku[row][col : col + 3]
                + sudoku[row + 1][col : col + 3]
                + sudoku[row + 2][col : col + 3]
            )
    # 박스 검사
    box_chk = 0 if 0 in set(map(chk, box)) else 1
    # 박스 에러
    if not box_chk:
        print(f'#{t} {0}')
        continue
    # 이상 없음
    print(f'#{t} {1}')
